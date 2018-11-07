import kivy
kivy.require("1.8.0")

from kivy.app import App

from kivy.core.window import Window
Window.size = (800, 600)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class PaintLayout(BoxLayout):
    def toto(self, *passed):
        print(s['pos'])
    #def on_touch_down(self, touch):
# with self.canvas:

class PaintApp(App):
    def build(self):
        return PaintLayout()


if __name__ == "__main__":
    PaintApp().run()
