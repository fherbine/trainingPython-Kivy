import kivy

kivy.require("1.8.0")

from kivy.app import App
from kivy.core.window import Window
#from kivy.uix.button import Label
from kivy.uix.widget import Widget

Window.size = (800, 600)

class NewWidget(Widget):
    pass

class MainApp(App):
    def build(self):
        return NewWidget() # Label <=> class Label(Widget) ???

if __name__ == "__main__":
    MainApp().run()
