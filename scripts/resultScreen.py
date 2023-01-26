from threading import Thread

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

import web_scraping


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)

        self.add_widget(Button(text='Go back to welcome screen', on_press=self.go_back))
        self.loading_animation = Image(source='../resources/loader.gif')
        self.add_widget(self.loading_animation)
        self.loading_animation.opacity = 0

    def on_enter(self):
        self.start_checking_rdv()

    def go_back(self, instance):
        # Get the screen manager from the kv file
        # Go back to the welcome screen (the one with name='welcome')
        self.manager.current = 'mainMenu'

    def start_checking_rdv(self):
        self.loading_animation.opacity = 1
        thread = Thread(target=self.checking_rdv)
        thread.start()

    def checking_rdv(self):
        print("start checking rdv")
        manager = App.get_running_app().root
        query = manager.get_screen('mainMenu').current_query

        if not query.is_set:
            self.stop_long_task()
        web_scraping.check_available_date(
            query.code_postal,
            query.distance,
            query.personnes
        )
        print("done.")
        self.stop_long_task()

    def stop_long_task(self):
        self.loading_animation.opacity = 0

        # sm = self.manager
        # sm.current = 'mainMenu'
