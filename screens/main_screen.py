from kivy.properties import ListProperty
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class ScreenMain(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=20, padding=[10])
        button_search = Button(
            size_hint=[1, .2],
            on_press=self._on_press_button_search,
            background_normal='data/забронировать место.png',
            border = (0, 0, 0, 0)
        )
        button_profil = Button(
            size_hint=[1, .18],
            on_press=self._on_press_button_profil,
            background_normal='data/мой профиль.png',
            border=(0, 0, 0, 0)
        )
        button_about = Button(
            size_hint=[.4, .4],
            on_press=self._on_press_button_about,
            background_normal='mylogo.png',
            border=(0, 0, 0, 0)
        )

        button_last_bron = Image(source='data/последняя бронь.png',
            size_hint=[1, .4],
        )

        button_bron_sdec_je = Button(
            size_hint=[1, .18],
            on_press=self._on_press_button_1,
            background_normal='data/забронировать здесь же.png',
            border=(0, 0, 0, 0)
        )

        boxlayout.add_widget(button_about)
        boxlayout.add_widget(button_last_bron)
        boxlayout.add_widget(button_bron_sdec_je)
        boxlayout.add_widget(button_profil)
        boxlayout.add_widget(button_search)
        self.add_widget(boxlayout)

    def _on_press_button_search(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'map_screen'

    def _on_press_button_profil(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'profil'

    def _on_press_button_about(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'about'

    def _on_press_button_1(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'parcing_screen_1'