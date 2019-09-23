import random
import string

import server_controllers.elements as elems

from configuration import STATIC_ELEMENTS


class GameMap:
    map_path = ''
    map_buffer = ''
    elements = []

    def __init__(self, path):
        self.map_path = path
        self.load_map()

    def load_map(self):
        self._read_map_file()
        self._load_elements_from_map()

    def reset_map(self):
        self.map_buffer = ''
        self.elements = []
        self.load_map()

    def add_player(self, skin):
        player = elems.UserElement(skin)
        empty_element = random.choice(
            [elem for elem in self.elements if (
                elem.__class__.__name__ == 'EmptyElement'
            )]
        )
        player.copy_element(empty_element)
        self.elements.append(player)

    def remove_player(self, player_skin):
        player = self.get_player_from_skin(player_skin)
        self.elements.remove(player)

    def generate_player_skin(self):
        ascii_upper = string.ascii_uppercase
        existing_skins = [elem.skin for elem in self.elements]
        available_skins = [
            char for char in ascii_upper if char not in existing_skins
        ]

        if not available_skins:
            return False

        return random.choice(available_skins)

    def get_player_from_skin(self, skin):
        for elem in self.elements:
            cls_name = elem.__class__.__name__
            if cls_name == 'UserElement' and elem.skin == skin:
                return elem
        return None

    def eval_command(self, player_skin, command, args):
        player = self.get_player_from_skin(player_skin)
        x, y = player.pos
        collide_elem = None

        if 'left' in command or 'O' in args:
            collide_elem = self._get_element_at_pos((x - 1, y))
        elif 'right' in command or 'E' in args:
            collide_elem = self._get_element_at_pos((x + 1, y))
        elif 'up' in command or 'N' in args:
            collide_elem = self._get_element_at_pos((x, y - 1))
        elif 'down' in command or 'S' in args:
            collide_elem = self._get_element_at_pos((x, y + 1))

        if not collide_elem:
            return False, ''

        player_cmd = getattr(player, command)

        if 'move' in command and collide_elem.collide:
            player_cmd()

            if collide_elem.__class__.__name__ == 'ArrivalElement':
                return True, '%WIN%'

        elif 'make' in command:
            if collide_elem.skin not in '.O':
                return False, ''

            player_cmd(collide_elem)
        else:
            return False, '%COLLIDE%'

        return True, '%OK%'

    def _get_element_at_pos(self, pos):
        for elem in self.elements:
            if elem.pos == pos:
                return elem

        return None

    def get_player_map(self, player_skin):
        player = self.get_player_from_skin(player_skin)
        self._update_map_buffer(player)
        return str(self)

    def __str__(self):
        tmp_buffer = [''.join(line) for line in self.map_buffer]
        return ''.join(tmp_buffer)

    def _update_map_buffer(self, player):
        for element in self.elements:
            x, y = element.pos

            self.map_buffer[y][x] = element.skin

        for element in self.elements:
            x, y = element.pos
            element_class = element.__class__.__name__

            if (
                element_class == 'UserElement'
                and element.skin != player.skin
            ):
                # comportement spécifique si joueur ennemi
                self.map_buffer[y][x] = element.skin.lower()
                continue

            self.map_buffer[y][x] = element.skin
        return self.map_buffer

    def _read_map_file(self):
        path = self.map_path

        with open(path) as map_file:
            tmp_buffer = map_file.readlines()

        if not tmp_buffer:
            raise Exception('`%s` est vide !' % path)

        tmp_buffer = [[char for char in line] for line in tmp_buffer]

        first_line = len(tmp_buffer[0])

        for line in tmp_buffer:
            if len(line) != first_line:
                raise Exception('`%s` est invalide !' % path)

        self.map_buffer = tmp_buffer

    def _load_elements_from_map(self):
        map_buffer = self.map_buffer

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
