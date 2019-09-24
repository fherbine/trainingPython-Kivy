from kivy.lang.builder import Builder
from kivy.properties import (
    ListProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.screenmanager import Screen

import widgets.tiles as tiles_classes


class PathFinderScreen(Screen):
    tiles_type = StringProperty()
    action = StringProperty()
    tiles = ListProperty()
    tile_class = ObjectProperty(allownone=True)
    container = ObjectProperty(allonone=True)
    departure_tile = ObjectProperty(allownone=True)
    arrival_tile = ObjectProperty(allownone=True)

    action_colors = {
        'arrival': (.2, 1, .2, 1),
        'departure': (1, .2, .2, 1),
        'wall': (0, 0, 0, 1),
    }

    def on_tiles_type(self, *_):
        if not self.tiles_type:
            return

        self.tile_class = getattr(tiles_classes, self.tiles_type)

    def fill_map(self):
        self.container.cols = self.w

        for y in range(self.h):
            for x in range(self.w):
                tile = self.tile_class(on_press=self.eval_tile)
                tile.tile_pos = (x, y)
                self.tiles.append(tile)
                self.container.add_widget(tile)

    def eval_tile(self, tile):
        if tile not in self.tiles or not self.action:
            return

        tile.color = self.action_colors[self.action]

        if self.action in ('arrival', 'departure'):
            setattr(self, self.action + '_tile', tile)
            self.action = ''

    def reset(self):
        self.container.clear_widgets()
        self.fill_map()


Builder.load_file('screens/path_finder.kv')
