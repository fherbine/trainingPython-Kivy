import json

from kivy.app import App
from kivy.properties import (
    BooleanProperty,
    ObjectProperty,
)

from screens import * # noqa
from widgets import * # noqa

class AstarApp(App):
    screenmanager = ObjectProperty(rebind=True)
    diagonals = BooleanProperty(False)

    def build(self):
        with open('settings.json') as settings_file:
            settings = json.load(settings_file)

        self.diagonals = settings.get('diagonals', False)

        self.screenmanager = self.root.screenmanager

if __name__ == '__main__':
    AstarApp().run()
