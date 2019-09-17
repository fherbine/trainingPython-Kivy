import sys

from kivy.app import App
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'system')

class TchatApp(App):
    def build(self):
        pass

if __name__ == '__main__':
    TchatApp().run()
