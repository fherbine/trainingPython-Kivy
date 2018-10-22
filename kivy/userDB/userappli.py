import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.core.window import Window
Window.size = (800, 600)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton # list of clickable buttons
from kivy.properties import ObjectProperty # similar as python class property it provides access to kv file

class UsersList(ListItemButton):
    pass

class BoxUserDB(BoxLayout):
    user_first_name = ObjectProperty()
    user_last_name = ObjectProperty()
    user_list = ObjectProperty()

    def new_user(self):
        pass

    def delete_user(self):
        pass

    def replace_user(self):
        pass

class UserDBApp(App):
    def build(self):
        return BoxUserDB()

if __name__ == "__main__":
    UserDBApp().run()
