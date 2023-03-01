from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class Profil(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        boxlayout = BoxLayout(orientation="vertical", spacing=20, padding=[10])

        button_back = Button(
            background_normal='data/назад.png',
            size_hint=[1, 0.2],
            on_press=self._on_press_button_back,
            border=(0, 0, 0, 0)
        )

        button_search = Button(
            size_hint=[1, .2],
            on_press=self._on_press_button_search,
            background_normal='data/забронировать место.png',
            border=(0, 0, 0, 0)
        )

        img = Image(source='noname_prof.png', )

        boxlayout.add_widget(img)
        boxlayout.add_widget(button_search)
        boxlayout.add_widget(button_back)
        self.add_widget(boxlayout)

    def _on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'

    def _on_press_button_search(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'map_screen'