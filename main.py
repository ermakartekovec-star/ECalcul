from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class ECalcul(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.display = TextInput(text='0', font_size=40, readonly=True)
        layout.add_widget(self.display)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        for row in buttons:
            hbox = BoxLayout()
            for label in row:
                btn = Button(text=label, font_size=30)
                btn.bind(on_press=self.on_button_press)
                hbox.add_widget(btn)
            layout.add_widget(hbox)
        
        return layout
    
    def on_button_press(self, instance):
        text = instance.text
        if text == '=':
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = 'Error'
        else:
            if self.display.text == '0' or self.display.text == 'Error':
                self.display.text = ''
            self.display.text += text

if __name__ == '__main__':
    ECalcul().run()
