import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Label

Window.size = (800, 600)

class HelloworldApp(App):

    def build(self):
        return Label()

if __name__ == "__main__":
    HelloworldApp().run()
