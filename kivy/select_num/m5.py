from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.garden.roulette import (
    Roulette,
    CyclicRoulette,
)

class SelectBox(BoxLayout):
    def recalculate_duration(self):
        self.duration = self.hms_duration['h'] * 3600 + self.hms_duration['m'] * 60 + self.hms_duration['s']

class SelectRoulette(Roulette):
    def __init__(self, **kwargs):
        super(SelectRoulette, self).__init__(**kwargs)
        self.background_image = None

class SelectCyclicRoulette(CyclicRoulette):
    def __init__(self, **kwargs):
        super(SelectCyclicRoulette, self).__init__(**kwargs)
        self.background_image = None

class M5App(App):
    def build(self):
        pass

if __name__ == "__main__":
    M5App().run()
