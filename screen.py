from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class Splash(Screen):

    def __init__(self):
        super().__init__()
        boxlayout = BoxLayout(orientation='vertical')
        mdlabel = MDLabel(text="Hasira")
        mdtoolbar = MDTopAppBar(title="Tour Ceylon")
        boxlayout.add_widget(mdtoolbar)
        boxlayout.add_widget(mdlabel)
        self.add_widget(boxlayout)