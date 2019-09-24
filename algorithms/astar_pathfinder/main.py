from kivy.app import App
from kivy.properties import ObjectProperty

from screens import * # noqa
from widgets import * # noqa

class AstarApp(App):
    screenmanager = ObjectProperty(rebind=True)

    def build(self):
        self.screenmanager = self.root.screenmanager

if __name__ == '__main__':
    AstarApp().run()
