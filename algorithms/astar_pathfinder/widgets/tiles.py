import math

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
    distance_to_arrival = NumericProperty()
    level = NumericProperty()

    def on_tile_pos(self, *_):
        self.tile_x, self.tile_y = self.tile_pos

    def get_h_dist(self, dst_tile):
        self.distance_to_arrival = self._distance_from_tile(dst_tile)

    def _distance_from_tile(self, tile):
        tx2, ty2 = tile.tile_pos

        return math.sqrt((tx2 - self.tile_x)**2 + (ty2 - self.tile_y)**2)



class NumberTile(Tile):
    pass

Builder.load_file('widgets/tiles.kv')
