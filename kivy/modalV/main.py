from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView


from kivy.clock import mainthread


class MainBox(BoxLayout):
    pass

class BoxContainer(BoxLayout):
    pass

class MyMV(ModalView):
    def __init__(self, **kwargs):
        super(MyMV, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.canvas.children = list()
        self.add_container()

    def add_container(self):
        self.add_widget(BoxContainer())

class MainApp(App):
    def build(self):
        pass

    def open_popup(self):
        popup = MyMV()
        popup.open()

if __name__ == '__main__':
        MainApp().run()
