import datetime
import hashlib
import os
import unittest

from server_controllers.server import (
    Server,
    ServerIhm,
)

class ServerTest(unittest.TestCase):
    pass

class ServerIhmTest(unittest.TestCase):
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
