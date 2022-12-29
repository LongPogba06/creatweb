import time

import kivy
from kivy.app import App
from kivy.lang import Builder


class MyApp(App):
    def build(self):
        return Builder.load_string(
    '''
    Label:
        font_sive: 32'''
        )
    def on_start(self):
        Clock.chedule_interval(
            self.update,1
        )
    def update(seft, *args):
        h = time.strftime("%H")
        m = time.strftime("%M")
        s = time.strftime("%S")
MyApp().run()
