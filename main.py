import sys
from screens.main_screen import ScreenMain
from screens.about_screen import About
from screens.prof_screen import Profil
from screens.map_screen import MapScreen_Lipetsk
from screens.parcing_screen_1 import Parcing_1
from screens.parcing_screen_2 import Parcing_2
from screens.parcing_screen_3 import Parcing_3
from screens.parcing_screen_4 import Parcing_4
from screens.parcing_screen_5 import Parcing_5
from screens.QR_screen import QR_screen

from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import mainthread, Clock


surname = ''
sm = ScreenManager()
main = ScreenMain(name='main_screen')
profil = Profil(name='profil')
about = About(name='about')
mapp = MapScreen_Lipetsk(name='map_screen')
parcing_1 = Parcing_1(name='parcing_screen_1')
parcing_2 = Parcing_2(name='parcing_screen_2')
parcing_3 = Parcing_3(name='parcing_screen_3')
parcing_4 = Parcing_4(name='parcing_screen_4')
parcing_5 = Parcing_5(name='parcing_screen_5')
qr_screen = QR_screen(name='qr_screen')
sm.add_widget(main)
sm.add_widget(qr_screen)
sm.add_widget(parcing_1)
sm.add_widget(parcing_2)
sm.add_widget(parcing_3)
sm.add_widget(parcing_4)
sm.add_widget(parcing_5)
sm.add_widget(profil)
sm.add_widget(about)
sm.add_widget(mapp)


class PaswordingApp(App):
    def build(self):
        Clock.schedule_once(self.set_background, 0)
        return sm

    def set_background(self, *args):
        self.root_window.bind()
        with self.root_window.canvas.before:
            self.bg = Rectangle(source='bgim.jpg', pos=(0, 0), size=(self.root_window.size))


number_type = 3
types = {1: "sat,skl",
         2: "sat",
         3: "map"
         }
if __name__ == "__main__":
    PaswordingApp().run()






