import datetime
import hashlib
import os
import unittest

from server_controllers.server import (
    GameCommands,
    Server,
    ServerIhm,
)

from server_controllers.elements import (
    ElementBase,
)

#=========== server_controlllers/server.py

class ServerTest(unittest.TestCase):
    pass


class GameCommandsTest(unittest.TestCase):
    """Tests pour le parser de commands GameCommands."""

    def test_simple_command(self):
        """Parsing d'une commande simple."""
        raw_cmd = 'e'

        cmd, args = GameCommands().parse_command(raw_cmd)
        self.assertEqual((cmd, args), ('move_right', ''))

    def test_command_with_arg(self):
        """Parsing d'une commande simple avec argument."""
        raw_cmd = 'ps'

        cmd, args = GameCommands().parse_command(raw_cmd)
        self.assertEqual((cmd, args), ('make_door', 'S'))

    def test_unknown_command(self):
        """Parsing d'une commande inexistante."""
        raw_cmd = 'l'

        cmd, args = GameCommands().parse_command(raw_cmd)
        self.assertEqual((cmd, args), (None, None))


class ServerIhmTest(unittest.TestCase):
    """Tests pour la classe ServerIhm."""

    def test_get_map_regular(self):
        """Test d'un cas fonctionnel (avec preselection de carte)"""
        server_ihm = ServerIhm()
        selected_map = server_ihm.get_map(pre_selected=0)

        self.assertEqual(selected_map, 'cartes/prison.txt')

    def test_get_map_unknown_folder(self):
        """Test de lecture de map sur un dossier inexistant."""

        # On génère le dossier inexistant à partir du md5 de la date actuel:
        # date actuel avec __str__
        date = str(datetime.datetime.now())
        # generation du md5
        fake_path = hashlib.md5(date.encode()).hexdigest()

        server_ihm = ServerIhm()
        server_ihm.maps_path = fake_path

        with self.assertRaises(Exception):
            selected_map = server_ihm.get_map(pre_selected=0)

    def test_get_map_empty_folder(self):
        """Test de lecture d'un dossier maps vide."""

        # On génère le dossier vide à partir du md5 de la date actuel:
        date = str(datetime.datetime.now())
        tmp_path = hashlib.md5(date.encode()).hexdigest()

        os.mkdir(tmp_path)

        server_ihm = ServerIhm()
        server_ihm.maps_path = tmp_path

        with self.assertRaises(Exception):
            selected_map = server_ihm.get_map(pre_selected=0)

        os.removedirs(tmp_path)

#=========== server_controlllers/elements.py

class ElementBaseTest(unittest.TestCase):
    """Test pour la classe ElementBase."""

    def test_pos_setter(self):
        element = ElementBase('#')
        element.pos = (80, 18)
        self.assertEqual(element.pos, (80, 18))

    def test_pos_x_setter(self):
        element = ElementBase('#')
        element.pos = (80, 18)
        self.assertEqual(element.x, 80)

    def test_pos_y_setter(self):
        element = ElementBase('#')
        element.pos = (80, 18)
        self.assertEqual(element.y, 18)

    def test_move_up_static(self):
        element = ElementBase('#')
        element.static = True
        element.pos = (80, 18)
        element.move_up()
        self.assertEqual(element.pos, (80, 18))

    def test_move_up_non_static(self):
        element = ElementBase('#')
        element.static = False
        element.pos = (80, 18)
        element.move_up()
        self.assertEqual(element.pos, (80, 17))

    def test_move_down_static(self):
        element = ElementBase('#')
        element.static = True
        element.pos = (80, 18)
        element.move_down()
        self.assertEqual(element.pos, (80, 18))

    def test_move_down_non_static(self):
        element = ElementBase('#')
        element.static = False
        element.pos = (80, 18)
        element.move_down()
        self.assertEqual(element.pos, (80, 19))

    def test_move_left_static(self):
        element = ElementBase('#')
        element.static = True
        element.pos = (80, 18)
        element.move_left()
        self.assertEqual(element.pos, (80, 18))

    def test_move_left_non_static(self):
        element = ElementBase('#')
        element.static = False
        element.pos = (80, 18)
        element.move_left()
        self.assertEqual(element.pos, (79, 18))

    def test_move_right_static(self):
        element = ElementBase('#')
        element.static = True
        element.pos = (80, 18)
        element.move_right()
        self.assertEqual(element.pos, (80, 18))

    def test_move_right_non_static(self):
        element = ElementBase('#')
        element.static = False
        element.pos = (80, 18)
        element.move_right()
        self.assertEqual(element.pos, (81, 18))

    def test_make_wall_skin(self):
        element = ElementBase('#')
        collide_element = ElementBase('.')

        collide_element.collide = True
        element.make_wall(collide_element)
        self.assertEqual(collide_element.skin, 'O')

    def test_make_wall_collide(self):
        element = ElementBase('#')
        collide_element = ElementBase('.')

        collide_element.collide = True
        element.make_wall(collide_element)
        self.assertEqual(collide_element.collide, False)

    def test_make_door_skin(self):
        element = ElementBase('#')
        collide_element = ElementBase('O')

        collide_element.collide = False
        element.make_door(collide_element)
        self.assertEqual(collide_element.skin, '.')

    def test_make_door_collide(self):
        element = ElementBase('#')
        collide_element = ElementBase('.')

        collide_element.collide = False
        element.make_door(collide_element)
        self.assertEqual(collide_element.collide, True)

    def test_copy_element(self):
        element = ElementBase('#')
        tocopy_element = ElementBase('.')
        element.pos = (21, 42)
        tocopy_element.pos = (42, 21)

        element.copy_element(tocopy_element)
        self.assertEqual(element.pos, tocopy_element.pos)

#=========== server_controlllers/game_map.py

class GameMapTest(unittest.TestCase):
    pass
