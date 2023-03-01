import random

from kivy.properties import ListProperty
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class Parcing_4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        l = Label(text="Студеновский карьер", font_size=20, bold=True)

        lg = Label(text="Колличество мест 30", font_size=20, bold=True)

        n = random.randint(0, 30)
        ll = Label(text=f"Свободно мест {n}", font_size=20, bold=True)

        button_search = Button(
            size_hint=[1, 1],
            on_press=self._on_press_button_pay,
            background_normal='data/забронировать место.png',
            border=(0, 0, 0, 0)
        )

        button_back = Button(
            background_normal='data/назад.png',
            size_hint=[1, 1],
            on_press=self._on_press_button_back,
            border=(0, 0, 0, 0)
        )

        l_1 = Label(text="", font_size=20)
        l_2 = Label(text="", font_size=20)

        boxlayout.add_widget(l)
        boxlayout.add_widget(lg)
        boxlayout.add_widget(ll)
        boxlayout.add_widget(button_search)
        boxlayout.add_widget(button_back)
        boxlayout.add_widget(l_1)
        boxlayout.add_widget(l_2)
        self.add_widget(boxlayout)

    def _on_press_button_pay(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'qr_screen'

    def _on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
