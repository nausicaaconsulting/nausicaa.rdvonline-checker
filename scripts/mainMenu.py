from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

from query import RdvQuery


class MainMenu(Screen):

    current_query = None

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.manager = App.get_running_app().root
        self.form_data = {}

        #
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #
        self.window.add_widget(Image(source='../resources/calendar_makyzz.png'))
        #
        self.postal_code_label = Label(
            text='Quel est votre code postal ?',
            font_size=18
        )
        self.postal_code = TextInput(
            multiline=False,
            size_hint=(1, 0.5),
        )
        self.window.add_widget(self.postal_code_label)
        self.window.add_widget(self.postal_code)
        self.window.add_widget(Label(size_hint=(1, 0.25)))
        #
        self.distance_label = Label(
            text='Quelle distance acceptez vous de parcourir ?',
            font_size=18
        )
        self.distance = TextInput(
            multiline=False,
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.distance_label)
        self.window.add_widget(self.distance)
        self.window.add_widget(Label(size_hint=(1, 0.25)))
        #
        self.nb_persons_label = Label(
            text='Pour combien de personnes prenez-vous le RDV ?',
            font_size=18
        )
        self.nb_persons = TextInput(
            multiline=False,
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.nb_persons_label)
        self.window.add_widget(self.nb_persons)
        self.window.add_widget(Label(size_hint=(1, 0.25)))
        #
        self.submit = Button(
            text='Rechercher',
            size_hint=(1, 0.5),
            bold=True,
            on_press=self.go_to_result_screen
        )
        self.window.add_widget(self.submit)

        self.add_widget(self.window)

    def go_to_result_screen(self, instance):
        self.current_query = RdvQuery()
        self.current_query.set_values(
            self.postal_code.text,
            self.distance.text,
            self.nb_persons.text
        )
        self.manager.current = 'result'
