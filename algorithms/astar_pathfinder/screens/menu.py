from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen


class MenuScreen(Screen):
    def do_pathfinder_calc_mode(self, width, height):
        app = App.get_running_app()
        screenmanager = app.screenmanager

        tile_class = 'NumberTile'

        screenmanager.current =  'path_finder'
        path_finder_screen = screenmanager.current_screen

        path_finder_screen.tiles_type = tile_class
        path_finder_screen.w = int(width)
        path_finder_screen.h = int(height)
        path_finder_screen.fill_map()


Builder.load_file('screens/menu.kv')
