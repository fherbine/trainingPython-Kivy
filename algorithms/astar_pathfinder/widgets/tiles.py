from kivy.lang.builder import Builder
from kivy.properties import (
    ListProperty,
    NumericProperty,
)
from kivy.uix.button import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout

class Tile(ButtonBehavior, FloatLayout):
    tile_pos = ListProperty()
    tile_x = NumericProperty()
    tile_y = NumericProperty()

    def on_tile_pos(self, *_):
        self.tile_x, self.tile_y = self.tile_pos

class NumberTile(Tile):
    pass

Builder.load_file('widgets/tiles.kv')
