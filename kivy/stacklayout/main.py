import kivy

kivy.require("1.8.0")

from kivy.app import App
from kivy.core.window import Window
Window.size = (800, 600)

from kivy.uix.stacklayout import StackLayout

class MainApp(App):
    def build(self):
        return StackLayout()

if __name__ == "__main__":
    MainApp().run()
