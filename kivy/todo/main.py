import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.core.window import Window
Window.size = (800, 600)

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class GridTodo(GridLayout, Label):
    def add(self, to_add):
        try:
            self.display.add_widget(Label(text=to_add))
        except:
            print("Error")

class TodoApp(App):
    def build(self):
        return GridTodo()

if __name__ == "__main__":
    TodoApp().run()
