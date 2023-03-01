from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class About(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        button_back = Button(
            background_normal='data/назад.png',
            size_hint=[1, .8],
            on_press=self._on_press_button_back,
            border=(0, 0, 0, 0)
        )

        l = Label(text="FPS - система умных",
                  font_size=25)
        l1 = Label(text="преднозначенная для",
                  font_size=25)
        l2 = Label(text="повышения скорости",
                  font_size=25)
        l3 = Label(text="поиска парковок и ",
                  font_size=25)
        l4 = Label(text="их автоматизации.",
                  font_size=25)

        boxlayout.add_widget(l)
        boxlayout.add_widget(l1)
        boxlayout.add_widget(l2)
        boxlayout.add_widget(l3)
        boxlayout.add_widget(l4)
        boxlayout.add_widget(button_back)
        self.add_widget(boxlayout)

    def _on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'