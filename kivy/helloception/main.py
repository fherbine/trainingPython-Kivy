import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.core.window import Window
Window.size = (800, 600)

from kivy.uix.gridlayout import GridLayout

class HWCeptionGridLayout(GridLayout):
    pass

class HWCeptionApp(App):
    def build(self):
        return HWCeptionGridLayout()

if __name__ == "__main__":
    HWCeptionApp().run()
