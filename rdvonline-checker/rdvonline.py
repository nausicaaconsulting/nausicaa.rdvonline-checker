from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from mainMenu import MainMenu
from resultScreen import ResultScreen


class ScreenManagerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='welcome'))
        sm.add_widget(ResultScreen(name='next'))
        return sm


if __name__ == '__main__':
    ScreenManagerApp().run()
