import kivy

kivy.require('2.0.0')

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#
# LOGIN SCREEN

class LoginScreen(Screen):
    pass

class Dashboard(Screen):
    pass

class WindowManager(ScreenManager):
    pass
#
# Main Program

class SysPyKV(MDApp):

    def build(self):
        return Builder.load_file('kv_files/loginscreen.kv')



if __name__ == '__main__':
    SysPyKV().run()
