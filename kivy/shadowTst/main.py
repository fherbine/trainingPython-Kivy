from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ListProperty


class ShadowLabel(Label):
    decal = ListProperty([0, 0])
    tint = ListProperty([1, 1, 1, 1])


class ShadowApp(App):
    pass


if __name__ == '__main__':
    ShadowApp().run()
