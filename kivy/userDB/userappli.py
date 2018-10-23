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
    user_age = ObjectProperty()
    user_list = ObjectProperty()

    def new_user(self):
        user = self.user_first_name.text + " " + self.user_last_name.text + " " + str(int(self.user_age.value))
        self.user_list.adapter.data.append(user)
        self.user_list._trigger_reset_populate() # resetting user list to refresh it

    def delete_user(self):
        selected_user = self.user_list.adapter.selection
        if selected_user:
            selected_user = selected_user[0].text
            self.user_list.adapter.data.remove(selected_user)
            self.user_list._trigger_reset_populate()

    def replace_user(self):
        selected_user = self.user_list.adapter.selection
        if selected_user:
            selected_user = selected_user[0].text
            user = self.user_first_name.text + " " + self.user_last_name.text + " " +str(int(self.user_age.value))
            idx = self.user_list.adapter.data.index(selected_user)
            self.user_list.adapter.data[idx] = user
            self.user_list._trigger_reset_populate()

class UserDBApp(App):
    def build(self):
        return BoxUserDB()

if __name__ == "__main__":
    UserDBApp().run()
