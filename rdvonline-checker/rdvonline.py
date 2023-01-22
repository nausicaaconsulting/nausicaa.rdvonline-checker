from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class RdvOnline(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        self.postal_code_label = Label(text='Quel est votre code postal ?')
        self.postal_code = TextInput(multiline=False)
        self.window.add_widget(self.postal_code_label)
        self.window.add_widget(self.postal_code)

        self.distance_label = Label(text='Quelle distance acceptez vous de parcourir ?')
        self.distance = TextInput(multiline=False)
        self.window.add_widget(self.distance_label)
        self.window.add_widget(self.distance)

        self.nb_persons_label = Label(text='Pour combien de personnes prenez-vous le RDV ?')
        self.nb_persons = TextInput(multiline=False)
        self.window.add_widget(self.nb_persons_label)
        self.window.add_widget(self.nb_persons)

        self.submit = Button(text='Rechercher')
        self.window.add_widget(self.submit)
        #add widgets to window

        return self.window


if __name__ == "__main__":
    RdvOnline().run()

#web_scraping.check_available_date(postal_code, distance, nb_persons)
