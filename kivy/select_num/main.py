from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.clock import mainthread
from kivy.properties import NumericProperty

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_move(self, touch):
        ''' Add selection on touch down '''
        print(touch, self.index)
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))

class NumSelectView(RecycleView):
    def __init__(self, **kwargs):
        super(NumSelectView, self).__init__(**kwargs)
        self.def_interval()

    @mainthread
    def def_interval(self):
        self.data = [{'text': str(x)} for x in range(self.limit_min, self.limit_max + 1)]

class SelNumApp(App):
    def build(self):
        pass
    
if __name__ == '__main__':
    SelNumApp().run() 
