from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout

class Tile(FloatLayout):
    pass

class NumberTile(Tile):
    pass

Builder.load_file('widgets/tiles.kv')
