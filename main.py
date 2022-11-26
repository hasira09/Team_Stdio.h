from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

Window.size = (310, 580)

sc = """
MDFloatLayout:
    md_bg_color: 1,1,1,1
    Carousel:
        id: carousel
        scroll_timeout:0
        on_current_slide: app.current_slide(self.index)
        MDFloatLayout:
            Image:
                source: "Images/BgImage2.jpg"
                pos_hint: {"center_x": .4, "center_y": .5}
                
            MDFloatLayout:
                Image:
                    source: "Images/TC_Logo.png"
                    pos_hint: {"center_x": .5, "center_y": .8}
                    size_hint: 1, .1
                    
                MDFloatLayout:    
                    Image:
                        source: "Images/Intro_T.png"
                        pos_hint: {"center_x": .5, "center_y": .67}
                        size_hint: 1, .1
                        
                    
                                        
"""


class TourCeylon(MDApp):

    def build(self):
        return Builder.load_string(sc)

    def current_slide(self, index):
        pass


if __name__ == "__main__":
    LabelBase.register(name="Inter", fn_regular="E:\PyCharm_Projects\SplashScren\FONTS\static\Inter-Regular.ttf")

    LabelBase.register(name="Inter", fn_regular="E:\PyCharm_Projects\SplashScren\FONTS\static\Inter-Bold.ttf")

TourCeylon().run()
