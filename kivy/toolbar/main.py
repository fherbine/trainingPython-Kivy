import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.core.window import Window
Window.size = (800, 600)

from kivy.uix.gridlayout import GridLayout

class GridToolbar(GridLayout):
    pass

class ToolbarApp(App):
    def build(self):
        return GridToolbar()

if __name__ == "__main__":
    ToolbarApp().run()
