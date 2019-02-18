from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.garden.roulettescroll import RouletteScrollEffect


from kivy.clock import mainthread
from kivy.base import runTouchApp

from kivy.properties import ObjectProperty, StringProperty

from kivy.factory import Factory


class SelectionLabel(Label):
    pass

class MainGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.amplitude = 3
        self.add_items()

    @mainthread
    def add_items(self):
        lbl = SelectionLabel(text='', height=self.parent.height / self.amplitude)
        self.add_widget(lbl)
        for i in range(5):
            lbl = SelectionLabel(text=str(i), height=self.parent.height / self.amplitude)
            self.add_widget(lbl)
        lbl = SelectionLabel(text='', height=self.parent.height / self.amplitude)
        self.add_widget(lbl)

    def switch_to_children(self, children_index):
        pass

class MyEffect(RouletteScrollEffect):
    def on_coasted_to_stop(self, *args):
        print('toto')

class MySV(ScrollView):
    container = ObjectProperty()
    selected_content = StringProperty('0')
    initial_value = StringProperty('0')

    def __init__(self, **kwargs):
        super(MySV, self).__init__(**kwargs)
        self.amplitude = 3
        self.effect_y = MyEffect(anchor=20, interval=40)
        self.effect_y.bind(on_coasted_to_stop=self.sstop)
        self.scroll_to_initial_value()

    @mainthread
    @mainthread
    def scroll_to_initial_value(self):
        for lbl in self.container.children:
            if lbl.text == self.initial_value:
                #self.scroll_to(lbl, padding=self.parent.height / self.amplitude)
                self.scroll_y = 0
                return True
        return False

    def sstop(self, *args):
        items_height = self.height / 3
        n_items = len(self.container.children)
        index = round(n_items * self.scroll_y)
        if index < (self.amplitude - 1) / 2:
            print('f')
            index = (self.amplitude - 1) / 2
        elif index > n_items - (self.amplitude - 1) / 2:
            print('s')
            index = n_items - (self.amplitude - 1) / 2

        index = int(index)
        selected_widget = self.container.children[index]
        self.selected_content = selected_widget.text
        scroll_item_target = items_height / (self.height * n_items) * self.scroll_y
        print('idx: ', index, n_items, self.scroll_y, self.selected_content)
        dy = self.convert_distance_to_scroll(0, index * self.height / 3)[1]
        print(dy)
        self.scroll_y = dy
        #self.scroll_to(selected_widget, padding=self.parent.height / self.amplitude)

class MainApp(App):
    def build(self):
        pass

if __name__ == "__main__":
    MainApp().run()
