from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

Window.size = (350, 600)


class TourCeylon(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
        self.title = "Tour-Ceylon"
        self.theme_cls.primary_palette = 'BlueGray'

        screen_manager.add_widget(Builder.load_file("splashs.kv"))
        screen_manager.add_widget(Builder.load_file("mainscreen.kv"))

        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen, 10)

    def change_screen(self, dt):
        screen_manager.current = "MainScreen"


TourCeylon().run()
