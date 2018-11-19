from os import chdir, getcwd, listdir

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import DictProperty, ObjectProperty
from kivy.uix.button import Button

class SubButtons(Button):
    def __init__(self, txt, **kwargs):
        super(SubButtons, self).__init__(**kwargs)
        self.text = txt
        size_hint = (None, .1)
        on_press

class ExplorerScreen(Screen):
    sub_container = ObjectProperty()

    def on_pre_enter(self):
        fresh_infos = App.get_running_app().get_dir_infos()
        ##self.refresh_dir_content(fresh_infos['ls'])

    def update_dir(self, path):
        chdir(path)
        fresh_infos = App.get_running_app().get_dir_infos()
        self.refresh_dir_content(fresh_infos['ls'])
    
    def refresh_dir_content(self, content):
        self.sub_container.clear_widgets()
        for sub in content:
            self.sub_container.add_widget(SubButtons(text=sub, size_hint=(None, .1), on_press=self.do_action("/")))

    def do_action(self, relative_pth):
        if 1 == 1:
            chdir(relative_pth)


class EditorScreen(Screen):
    pass

class ScreenHandler(ScreenManager):
    pass

class FlexApp(App):
    dirInfos = DictProperty()

    def build(self):
        self.root.current = 'explorer'
        self.get_dir_infos()

    def get_dir_infos(self):
        self.dirInfos['cd'] = getcwd()
        self.dirInfos['ls'] = listdir()
        return self.dirInfos



if __name__ == "__main__":
    FlexApp().run()
