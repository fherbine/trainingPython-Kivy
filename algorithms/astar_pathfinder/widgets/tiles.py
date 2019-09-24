from kivy.lang.builder import Builder
from kivy.uix.button import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout

class Tile(ButtonBehavior, FloatLayout):
    pass

class NumberTile(Tile):
    pass

Builder.load_file('widgets/tiles.kv')
