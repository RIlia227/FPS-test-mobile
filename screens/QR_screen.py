import random

from kivy.properties import ListProperty
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class QR_screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        boxlayout = BoxLayout(orientation="vertical", spacing=20, padding=[10])

        button_last_bron = Image(source=f'Qr_cods/chart{random.randint(0, 4)}.png')

        l = Label(text="QR-код для въезда", font_size=20, bold=True)

        button_back = Button(
            background_normal='data/назад.png',
            size_hint=[1, .3],
            on_press=self._on_press_button_back,
            border=(0, 0, 0, 0)
        )

        boxlayout.add_widget(button_last_bron)
        boxlayout.add_widget(l)
        boxlayout.add_widget(button_back)
        self.add_widget(boxlayout)

    def _on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
