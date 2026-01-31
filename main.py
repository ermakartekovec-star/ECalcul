from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        self.result = TextInput(text="0", readonly=True, font_size=32, halign="right")
        main_layout.add_widget(self.result)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
            ['=']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, font_size=32, on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        return main_layout
    
    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.result.text = str(eval(self.expression))
            except:
                self.result.text = "Error"
            self.expression = ""
        elif instance.text == 'C':
            self.expression = ""
            self.result.text = "0"
        else:
            if self.result.text == "0" or self.result.text == "Error":
                self.result.text = ""
            self.expression += instance.text
            self.result.text = self.expression

if __name__ == "__main__":
    CalculatorApp().run()
