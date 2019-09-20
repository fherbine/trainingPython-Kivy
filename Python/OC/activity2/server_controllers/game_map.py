import random

import server_controllers.elements as elems

from configuration import STATIC_ELEMENTS


class GameMap:
    map_buffer = ''
    elements = []

    def __init__(self, path):
        self.load_map(path)

    def load_map(self, path):
        self._read_map_file(path)
        self._load_elements_from_map()

    def add_player(self, skin):
        player = PlayerElement(skin)
        empty_element = random.choice(
            [elem for elem in self.elements if (
                elem.__class__.__name__ == 'EmptyElement'
            )]
        )
        player.copy_element(empty_element)
        self.elements.remove(empty_element)
        self.elements.append(player)
        return player

    def get_player_map(self, player)
        return self._update_map_buffer(player)

    def __str__(self):
        self.update_map_buffer()

        return map_buffer

    def _update_map_buffer(self, player):
        for element in self.elements:
            x, y = element.pos
            element_class = element.__class__.__name__

            if (
                element_class == 'PlayerElement'
                and element.skin != player.skin
            ):
                # comportement spécifique si joueur ennemi
                self.map_buffer[y][x] = element.skin.lower()
                continue

            self.map_buffer[y][x] = element.skin
        return self.map_buffer

    def _read_map_file(self, path):
        with open(path) as map_file:
            tmp_buffer = map_file.readlines()

        if not tmp_buffer:
            raise Exception('`%s` est vide !' % path)

        first_line = len(tmp_buffer[0])

        for line in tmp_buffer:
            if len(line) != first_line:
                raise Exception('`%s` est invalide !')

        self.map_buffer = tmp_buffer

    def _load_elements_from_map():
        for y, line in enumerate(map_buffer):
            for x, char in enumerate(line):
                if char == '\n':
                    continue

                if char in STATIC_ELEMENTS:
                    ElementClass = getattr(elems, STATIC_ELEMENTS[char])
                else:
                    ElementsClass = elems.EmptyElement

                element = ElementClass()
                element.pos = (x, y)
                self.elements.append(element)
