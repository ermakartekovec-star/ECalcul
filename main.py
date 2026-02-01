from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import math
import json
import os
from datetime import datetime

class ECalcul(App):
    def build(self):
        self.title = "E-Calcul - Супер калькулятор"
        Window.size = (400, 700)
        
        # Основной контейнер
        main_layout = BoxLayout(orientation='vertical', spacing=5, padding=10)
        
        # История и память
        self.history = []
        self.memory = 0
        
        # Верхняя панель: экран и память
        top_panel = BoxLayout(size_hint=(1, 0.15))
        
        # Экран ввода/вывода
        self.display = TextInput(
            text='0',
            font_size=32,
            halign='right',
            readonly=True,
            multiline=False,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1)
        )
        
        # Кнопка памяти
        mem_btn = Button(
            text='M: 0',
            font_size=16,
            on_press=self.show_memory_menu
        )
        
        top_panel.add_widget(self.display)
        top_panel.add_widget(mem_btn)
        main_layout.add_widget(top_panel)
        
        # История (прокручиваемая)
        history_scroll = ScrollView(size_hint=(1, 0.2))
        self.history_label = Label(
            text='История:\n',
            font_size=14,
            halign='left',
            valign='top',
            size_hint_y=None,
            text_size=(380, None)
        )
        self.history_label.bind(texture_size=self.history_label.setter('size'))
        history_scroll.add_widget(self.history_label)
        main_layout.add_widget(history_scroll)
        
        # Панель вкладок
        self.tabs = TabbedPanel(do_default_tab=False)
        
        # Вкладки
        self.create_basic_tab()
        self.create_scientific_tab()
        self.create_converter_tab()
        
        main_layout.add_widget(self.tabs)
        
        # Нижняя панель: дополнительные функции
        bottom_panel = BoxLayout(size_hint=(1, 0.1))
        bottom_panel.add_widget(Button(text='История', on_press=self.show_history))
        bottom_panel.add_widget(Button(text='Очистить', on_press=self.clear_all))
        bottom_panel.add_widget(Button(text='Настройки', on_press=self.show_settings))
        main_layout.add_widget(bottom_panel)
        
        # Текущее выражение
        self.current_expression = ''
        
        return main_layout
    
    # ========== ОСНОВНАЯ ВКЛАДКА ==========
    def create_basic_tab(self):
        tab = TabbedPanelItem(text='Основной')
        layout = GridLayout(cols=4, spacing=5)
        
        # Кнопки основного калькулятора
        buttons = [
            'C', '⌫', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '±', '0', '.', '='
        ]
        
        for btn_text in buttons:
            btn = Button(
                text=btn_text,
                font_size=24,
                background_color=self.get_button_color(btn_text)
            )
            btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)
        
        tab.add_widget(layout)
        self.tabs.add_widget(tab)
    
    # ========== НАУЧНАЯ ВКЛАДКА ==========
    def create_scientific_tab(self):
        tab = TabbedPanelItem(text='Научный')
        layout = GridLayout(cols=5, spacing=5)
        
        sci_buttons = [
            'sin', 'cos', 'tan', 'log', 'ln',
            'x²', 'x³', '√', '∛', 'π',
            'e', 'x!', '10^x', 'e^x', '|x|',
            '(', ')', 'mod', 'rand', 'deg'
        ]
        
        for btn_text in sci_buttons:
            btn = Button(
                text=btn_text,
                font_size=18,
                background_color=(0.3, 0.5, 0.7, 1)
            )
            btn.bind(on_press=self.on_sci_button_press)
            layout.add_widget(btn)
        
        tab.add_widget(layout)
        self.tabs.add_widget(tab)
    
    # ========== КОНВЕРТЕР ВКЛАДКА ==========
    def create_converter_tab(self):
        tab = TabbedPanelItem(text='Конвертер')
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Выбор типа конвертации
        self.conv_type = Spinner(
            text='Валюта',
            values=['Валюта', 'Длина', 'Вес', 'Температура', 'Площадь'],
            size_hint=(1, 0.1)
        )
        self.conv_type.bind(text=self.on_conv_type_change)
        
        # Поля ввода
        input_box = BoxLayout(size_hint=(1, 0.2))
        self.conv_input = TextInput(text='1', font_size=24, halign='right')
        self.conv_from = Spinner(text='USD', values=['USD', 'EUR', 'RUB', 'CNY'])
        input_box.add_widget(self.conv_input)
        input_box.add_widget(self.conv_from)
        
        # Поля вывода
        output_box = BoxLayout(size_hint=(1, 0.2))
        self.conv_output = TextInput(text='90', font_size=24, readonly=True, halign='right')
        self.conv_to = Spinner(text='RUB', values=['USD', 'EUR', 'RUB', 'CNY'])
        output_box.add_widget(self.conv_output)
        output_box.add_widget(self.conv_to)
        
        # Кнопка конвертации
        conv_btn = Button(
            text='Конвертировать',
            font_size=20,
            background_color=(0.2, 0.7, 0.3, 1),
            on_press=self.convert_value
        )
        
        layout.add_widget(self.conv_type)
        layout.add_widget(Label(text='Из:'))
        layout.add_widget(input_box)
        layout.add_widget(Label(text='В:'))
        layout.add_widget(output_box)
        layout.add_widget(conv_btn)
        
        tab.add_widget(layout)
        self.tabs.add_widget(tab)
    
    # ========== ОБРАБОТЧИКИ КНОПОК ==========
    def on_button_press(self, instance):
        btn_text = instance.text
        
        if btn_text == 'C':
            self.current_expression = ''
            self.display.text = '0'
        
        elif btn_text == '⌫':
            if len(self.current_expression) > 0:
                self.current_expression = self.current_expression[:-1]
                self.display.text = self.current_expression if self.current_expression else '0'
        
        elif btn_text == '=':
            try:
                result = str(eval(self.current_expression.replace('π', str(math.pi))))
                self.history.append(f"{self.current_expression} = {result}")
                self.update_history()
                self.current_expression = result
                self.display.text = result
            except:
                self.display.text = 'Ошибка'
                self.current_expression = ''
        
        elif btn_text == '±':
            if self.display.text and self.display.text != '0':
                if self.display.text[0] == '-':
                    self.display.text = self.display.text[1:]
                else:
                    self.display.text = '-' + self.display.text
                self.current_expression = self.display.text
        
        else:
            if self.display.text == '0' or self.display.text == 'Ошибка':
                self.display.text = ''
            
            self.current_expression += btn_text
            self.display.text = self.current_expression
    
    def on_sci_button_press(self, instance):
        btn_text = instance.text
        x = self.get_current_number()
        
        try:
            if btn_text == 'sin': result = math.sin(math.radians(x))
            elif btn_text == 'cos': result = math.cos(math.radians(x))
            elif btn_text == 'tan': result = math.tan(math.radians(x))
            elif btn_text == 'log': result = math.log10(x) if x > 0 else 'Ошибка'
            elif btn_text == 'ln': result = math.log(x) if x > 0 else 'Ошибка'
            elif btn_text == 'x²': result = x ** 2
            elif btn_text == 'x³': result = x ** 3
            elif btn_text == '√': result = math.sqrt(x) if x >= 0 else 'Ошибка'
            elif btn_text == '∛': result = x ** (1/3)
            elif btn_text == 'π': result = math.pi
            elif btn_text == 'e': result = math.e
            elif btn_text == 'x!': result = math.factorial(int(x)) if x >= 0 else 'Ошибка'
            elif btn_text == '10^x': result = 10 ** x
            elif btn_text == 'e^x': result = math.exp(x)
            elif btn_text == '|x|': result = abs(x)
            elif btn_text == 'mod': 
                self.current_expression += ' % '
                self.display.text = self.current_expression
                return
            elif btn_text == 'rand': result = round(math.random(), 4)
            elif btn_text == 'deg': result = math.degrees(x)
            else: result = btn_text
            
            if result != btn_text:
                self.history.append(f"{btn_text}({x}) = {result}")
                self.update_history()
                self.display.text = str(result)
                self.current_expression = str(result)
            else:
                self.current_expression += btn_text
                self.display.text = self.current_expression
                
        except:
            self.display.text = 'Ошибка'
    
    # ========== КОНВЕРТЕР ==========
    def on_conv_type_change(self, spinner, text):
        if text == 'Валюта':
            self.conv_from.values = ['USD', 'EUR', 'RUB', 'CNY', 'JPY', 'GBP']
            self.conv_to.values = ['USD', 'EUR', 'RUB', 'CNY', 'JPY', 'GBP']
            self.conv_from.text = 'USD'
            self.conv_to.text = 'RUB'
        elif text == 'Длина':
            self.conv_from.values = ['m', 'km', 'cm', 'mm', 'mile', 'foot']
            self.conv_to.values = ['m', 'km', 'cm', 'mm', 'mile', 'foot']
            self.conv_from.text = 'm'
            self.conv_to.text = 'km'
    
    def convert_value(self, instance):
        try:
            value = float(self.conv_input.text)
            conv_type = self.conv_type.text
            
            if conv_type == 'Валюта':
                rates = {'USD': 90.0, 'EUR': 98.0, 'RUB': 1.0, 
                        'CNY': 12.5, 'JPY': 0.6, 'GBP': 115.0}
                from_rate = rates.get(self.conv_from.text, 1)
                to_rate = rates.get(self.conv_to.text, 1)
                result = value * to_rate / from_rate
            
            elif conv_type == 'Длина':
                units = {'m': 1, 'km': 1000, 'cm': 0.01, 
                        'mm': 0.001, 'mile': 1609.34, 'foot': 0.3048}
                result = value * units[self.conv_from.text] / units[self.conv_to.text]
            
            self.conv_output.text = str(round(result, 4))
            self.history.append(f"{value} {self.conv_from.text} = {result} {self.conv_to.text}")
            self.update_history()
            
        except:
            self.conv_output.text = 'Ошибка'
    
    # ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==========
    def get_button_color(self, text):
        if text in ['C', '⌫', '%']:
            return (0.8, 0.4, 0.4, 1)
        elif text in ['/', '*', '-', '+', '=']:
            return (0.4, 0.6, 0.8, 1)
        elif text == '±':
            return (0.6, 0.6, 0.6, 1)
        else:
            return (0.3, 0.3, 0.3, 1)
    
    def get_current_number(self):
        try:
            return float(self.display.text)
        except:
            return 0.0
    
    def show_memory_menu(self, instance):
        popup = Popup(title='Память', size_hint=(0.8, 0.4))
        content = BoxLayout(orientation='vertical')
        
        content.add_widget(Label(text=f'Текущее значение: {self.memory}'))
        
        btn_layout = GridLayout(cols=2)
        btn_layout.add_widget(Button(text='M+', on_press=lambda x: self.memory_add()))
        btn_layout.add_widget(Button(text='M-', on_press=lambda x: self.memory_subtract()))
        btn_layout.add_widget(Button(text='MR', on_press=lambda x: self.memory_recall()))
        btn_layout.add_widget(Button(text='MC', on_press=lambda x: self.memory_clear()))
        
        content.add_widget(btn_layout)
        content.add_widget(Button(text='Закрыть', on_press=lambda x: popup.dismiss()))
        
        popup.content = content
        popup.open()
    
    def memory_add(self):
        try:
            self.memory += float(self.display.text)
        except:
            pass
    
    def memory_subtract(self):
        try:
            self.memory -= float(self.display.text)
        except:
            pass
    
    def memory_recall(self):
        self.display.text = str(self.memory)
        self.current_expression = str(self.memory)
    
    def memory_clear(self):
        self.memory = 0
    
    def show_history(self, instance):
        popup = Popup(title='История вычислений', size_hint=(0.9, 0.7))
        content = ScrollView()
        
        history_text = '\n'.join(self.history[-20:]) if self.history else 'История пуста'
        label = Label(
            text=history_text,
            font_size=18,
            halign='left',
            valign='top',
            size_hint_y=None,
            text_size=(350, None)
        )
        label.bind(texture_size=label.setter('size'))
        
        content.add_widget(label)
        popup.content = content
        popup.open()
    
    def update_history(self):
        history_text = 'История:\n' + '\n'.join(self.history[-5:])
        self.history_label.text = history_text
    
    def clear_all(self, instance):
        self.current_expression = ''
        self.display.text = '0'
        self.history = []
        self.update_history()
    
    def show_settings(self, instance):
        popup = Popup(title='Настройки', size_hint=(0.8, 0.6))
        content = BoxLayout(orientation='vertical')
        
        content.add_widget(Label(text='Тема:'))
        theme_switch = Switch(active=True)
        content.add_widget(theme_switch)
        
        content.add_widget(Label(text='Размер шрифта:'))
        font_slider = Slider(min=10, max=40, value=24)
        font_slider.bind(value=self.change_font_size)
        content.add_widget(font_slider)
        
        content.add_widget(Button(text='Сохранить', on_press=lambda x: popup.dismiss()))
        popup.content = content
        popup.open()
    
    def change_font_size(self, instance, value):
        self.display.font_size = value

if __name__ == '__main__':
    ECalcul().run()
