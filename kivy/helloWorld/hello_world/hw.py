import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Label
from kivy.core.window import Window

Window.size = (1120, 630)


class HelloWorldApp(App):
    
    def build(self):
        return Label(text="Hello World !")

if __name__ == '__main__':
    HelloWorldApp().run()
