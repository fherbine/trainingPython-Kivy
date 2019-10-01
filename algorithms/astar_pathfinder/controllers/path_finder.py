import math
import copy
from functools import partial

from kivy.app import App
from kivy.clock import mainthread
from kivy.event import EventDispatcher
from kivy.properties import (
    DictProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)


class PathFinder(EventDispatcher):
    best_path = DictProperty()
    tiles = ListProperty()
    departure_tile = ObjectProperty(allownone=True)
    arrival_tile = ObjectProperty(allownone=True)
    diagonals = True
    level = NumericProperty()

    def _special_copy(self, dictn):
        """Because Kivy doesn't accept deepcopy.

        Special use case do NOT use for recursive for recursive copy operation.
        """

        new_dict = dict()

        new_dict = {copy.copy(key): copy.copy(value) for key, value in dictn.items()}

        return new_dict

    @mainthread
    def on_arrival_tile(self, *_):
        if not self.arrival_tile:
            return

        self.best_weight = self.xmap * self.ymap * 100
        current_path = {'path': [], 'weight': 0}
        self.best_path = self.pathfinder(
            self.departure_tile,
            self.arrival_tile,
            current_path,
        )
        print([tile for tile in self.best_path['path']])
        print(self.best_path['weight'])


    def pathfinder(self, tile, dst_tile, current_path, g_dist=0):
        current_path['path'].append(tile.tile_pos)
        tile.get_h_dist(dst_tile)
        h_dist = tile.distance_to_arrival
        total_weight = g_dist + h_dist
        #optional
        tile.f = round(total_weight, 2)
        tile.h = round(h_dist, 2)
        tile.g = round(g_dist, 2)
        tile.color = total_weight/100, h_dist/100, g_dist, 1
        ###
        current_path['weight'] += total_weight
        accessible_tiles = self._list_accessible_tiles(tile, current_path, g_dist, dst_tile)
        current_path = self._get_better_accessible(accessible_tiles, current_path)


        if not accessible_tiles or current_path['weight'] > self.best_weight:
            return None

        elif dst_tile in accessible_tiles:
            self.best_weight = current_path['weight']
            current_path['path'].append(dst_tile.tile_pos)
            return current_path

        paths = list()

        b_path = None

        for a_tile in accessible_tiles:
            copied_cpath = self._special_copy(current_path)
            b_path = self.pathfinder(
                a_tile,
                dst_tile,
                copied_cpath,
                g_dist + tile._distance_from_tile(a_tile),
            )
            if b_path is not None:
                break


        return b_path

    def _keep_best_path(self, paths):
        if not paths:
            return None

        lighter = paths[0]

        for path in paths:
            if path['weight'] < lighter['weight']:
                lighter = path

        return lighter

    def _get_better_accessible(self, accessible, current_path):
        already_in_path = []


        for tile in accessible:
            if tile.tile_pos in current_path['path']:
                already_in_path.append(tile)


        already_in_path.sort(key=lambda tile: tile.g)
        for tile  in accessible:
            if tile.tile_pos in current_path['path']:
                accessible.remove(tile)

        if already_in_path:
            already_in_path.pop(0).tile_pos

        for tile in already_in_path:
            current_path['path'].remove(tile.tile_pos)

        return current_path

    def _list_accessible_tiles(self, tile, current_path, g_dist,dst):
        accessible = []
        tx, ty = tile.tile_pos

        top_tile = self.get_tile_from_coordinate(tx, ty-1)
        bottom_tile = self.get_tile_from_coordinate(tx, ty+1)
        left_tile = self.get_tile_from_coordinate(tx-1, ty)
        right_tile = self.get_tile_from_coordinate(tx+1, ty)

        accessible = [top_tile, bottom_tile, left_tile, right_tile]
        accessible = [atile for atile in accessible if atile is not None and self._is_tile_wakable(atile)]
        accessible_tuples = list(zip(accessible, [1] * len(accessible)))

        if not self.diagonals:
            sorted_list = self._sort_accessible([(atile, g) for atile, g in accessible_tuples], g_dist, dst, current_path)
            if not self._is_tiles_wakable_in_list(sorted_list):
                return None
            return sorted_list

        if top_tile in accessible or right_tile in accessible:
            dtile = self.get_tile_from_coordinate(tx+1, ty-1)
            if dtile is not None:
                accessible_tuples.append((dtile, math.sqrt(2)))

        if top_tile in accessible or left_tile in accessible:
            dtile = self.get_tile_from_coordinate(tx-1, ty-1)
            if dtile is not None:
                accessible_tuples.append((dtile, math.sqrt(2)))

        if bottom_tile in accessible or right_tile in accessible:
            dtile = self.get_tile_from_coordinate(tx+1, ty+1)
            if dtile is not None:
                accessible_tuples.append((dtile, math.sqrt(2)))

        if bottom_tile in accessible or left_tile in accessible:
            dtile = self.get_tile_from_coordinate(tx-1, ty+1)
            if dtile is not None:
                accessible_tuples.append((dtile, math.sqrt(2)))


        sorted_list = self._sort_accessible([(atile, g) for atile, g in accessible_tuples if self._is_tile_wakable(atile)], g_dist, dst, current_path)
        return sorted_list

    def _sort_accessible(self, accessible, g_dist, dst, current_path):
        acces = list()
        for tile, g in accessible:
            if tile.tile_pos not in current_path['path']:
                tile.g = round(g_dist + g, 2)
            acces.append(tile)

        sort = sorted(acces, key=lambda src: self._distance_from_tile(src, dst) + src.g)

        return sort


    def _distance_from_tiles(self, src_tile, *tiles):
        return [
            (tile, self._distance_from_tile(src_tile, tile)) for tile in tiles
        ]

    def _distance_from_tile(self, tile1, tile2):
        tx1, ty1 = tile1.tile_pos
        tx2, ty2 = tile2.tile_pos

        return math.sqrt((tx2 - tx1)**2 + (ty2 - ty1)**2)

    def _is_tiles_wakable_in_list(self, tiles):
        for tile in tiles:
            if not self._is_tile_wakable(tile):
                return False
        return True

    def _is_tile_wakable(self, tile):
        if tile.level > self.level:
            return False
        return True

    def get_tile_from_coordinate(self, tx, ty):
        if not (0 <= ty < len(self.tiles)) or not (0 <= tx < len(self.tiles[0])):
            return None

        return self.tiles[ty][tx]
