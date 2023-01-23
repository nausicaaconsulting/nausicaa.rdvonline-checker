from threading import Thread

from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.image import Image

from kivy.uix.screenmanager import Screen


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        #self.add_widget(Button(text='Go back to welcome screen', on_press=self.go_back))
        self.loading_animation = Image(source='../resources/loader.gif')
        self.add_widget(self.loading_animation)
        self.loading_animation.opacity = 0
        self.start_long_task()

    def go_back(self, instance):
        # Get the screen manager from the kv file
        sm = self.manager
        # Go back to the welcome screen (the one with name='welcome')
        sm.current = 'welcome'

    def start_long_task(self):
        self.loading_animation.opacity = 1
        thread = Thread(target=self.long_task)
        thread.start()

    def long_task(self):
        # do long task here
        # ...
        Clock.schedule_once(self.stop_long_task, 5)  # stop after 10 seconds
        #web_scraping.check_available_date(postal_code, distance, nb_persons)
    def stop_long_task(self, dt):
        self.loading_animation.opacity = 0
        # continue with other stuff
        # test
        sm = self.manager
        sm.current = 'welcome'
