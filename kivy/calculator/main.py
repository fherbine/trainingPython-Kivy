import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.core.window import Window
Window.size = (800, 600)

from kivy.uix.gridlayout import GridLayout

class CalcGrid(GridLayout):

    def do_op(self, ope):
        if ope:
            try:
                self.display.text = str(eval(ope))
            except:
                self.display.text = "Error"

class CalcApp(App):
    def build(self):
        return CalcGrid()

if __name__ == "__main__":
    CalcApp().run()
