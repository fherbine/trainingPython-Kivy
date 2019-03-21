from kivy.app import App

import toto

from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.window import Window


class MainApp(App):
    def build(self):
        self.keyboard = Window.request_keyboard(None, self)
        self.keyboard.bind(on_key_down=self.on_keyboard_down)

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'f2':
            toto.TotoApp().run()
        else:
            print(keycode)


class MainButton(Button):
    def on_press(self, *largs, **kwargs):
        Clock.schedule_once(self.launch_toto, .50)

    def on_key_down(self, *largs, **kwargs):
        print(largs, kwargs)

    def launch_toto(self, dt):
        toto.TotoApp().run()

if __name__ == '__main__':
    MainApp().run()
    print('runned')
