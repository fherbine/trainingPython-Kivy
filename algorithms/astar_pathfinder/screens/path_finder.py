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
    tiles = ListProperty()
    tile_class = ObjectProperty(allownone=True)
    container = ObjectProperty(allonone=True)

    def on_tiles_type(self, *_):
        if not self.tiles_type:
            return

        self.tile_class = getattr(tiles_classes, self.tiles_type)

    def fill_map(self):
        for _ in range(self.w * self.h):
            tile = self.tile_class()
            self.tiles.append(tile)
            self.container.add_widget(tile)


Builder.load_file('screens/path_finder.kv')
