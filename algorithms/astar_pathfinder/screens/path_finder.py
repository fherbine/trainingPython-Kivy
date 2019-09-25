from kivy.lang.builder import Builder
from kivy.properties import (
    DictProperty,
    ListProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.screenmanager import Screen

import widgets.tiles as tiles_classes

from controllers.path_finder import PathFinder


class PathFinderScreen(Screen):
    tiles_type = StringProperty()
    action = StringProperty()
    tiles = ListProperty()
    tile_class = ObjectProperty(allownone=True)
    container = ObjectProperty(allonone=True)
    departure_tile = ObjectProperty(allownone=True)
    arrival_tile = ObjectProperty(allownone=True)
    best_path = DictProperty()

    action_colors = {
        'arrival': (.2, 1, .2, 1),
        'departure': (1, .2, .2, 1),
        'wall': (0, 0, 0, 1),
    }

    def on_best_path(self, *_):
        if not self.best_path:
            return
        else:
            for tile_pos in self.best_path['path']:
                tile = self.path_finder.get_tile_from_coordinate(*tile_pos)
                tile.color = 0, 1, 0, 1

    def on_tiles_type(self, *_):
        if not self.tiles_type:
            return

        self.tile_class = getattr(tiles_classes, self.tiles_type)
        self.path_finder = path_finder = PathFinder()
        self.path_finder.bind(best_path=lambda *_:self.setter(
            'best_path'
        )(_, self.path_finder.best_path))
        self.bind(
            tiles=lambda *_: self.path_finder.setter('tiles')(_, self.tiles)
        )

    def fill_map(self):
        self.container.cols = self.w
        self.path_finder.xmap = self.w
        self.path_finder.ymap = self.h

        for y in range(self.h):
            self.tiles.append(list())
            for x in range(self.w):
                tile = self.tile_class(on_press=self.eval_tile)
                tile.tile_pos = (x, y)
                self.tiles[y].append(tile)
                self.container.add_widget(tile)


    def eval_tile(self, tile):
        if not self.action:
            return


        tile.color = self.action_colors[self.action]
        tile.level = 1 if self.action == 'wall' else 0

        if self.action in ('arrival', 'departure'):
            setattr(self, self.action + '_tile', tile)
            setattr(self.path_finder, self.action + '_tile', tile)
            self.action = ''

    def reset(self):
        self.tiles = []
        self.container.clear_widgets()
        self.fill_map()


Builder.load_file('screens/path_finder.kv')
