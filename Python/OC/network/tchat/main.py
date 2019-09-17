import sys

from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    ObjectProperty,
)

from client import Client
from variables import HOST

Config.set('kivy', 'keyboard_mode', 'system')

class TchatApp(App):
    cnx = ObjectProperty(allownone=True)
    unread_in_waiting = BooleanProperty(False)
    message_data = ListProperty()

    def build(self):
        self.cnx = cnx = Client()
        Clock.schedule_interval(self.check_unread, .5)

    def send_message(self, msg):
        cnx = self.cnx
        cnx.send_message(msg)
        self.unread_in_waiting = True

    def check_unread(self, dt):
        if not self.unread_in_waiting:
            return

        cnx = self.cnx
        msg = cnx.get_message()

        if msg == 'QUIT':
            self.stop()

        self.message_data.append({'src': str(HOST), 'content': msg})

        self.unread_in_waiting = False

    def on_stop(self):
        cnx = self.cnx
        cnx.close_all()


if __name__ == '__main__':
    TchatApp().run()
