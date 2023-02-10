from kivy.app import App
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.clock import mainthread
from kivy.core.clipboard import Clipboard as Cb
import threading
import socket

KV = """
MyBL:
	orientation: "vertical"
	size_hint: (0.95, 0.95)
	pos_hint: {"center_x": 0.5, "center_y":0.5}

	Label:
		font_size: "15sp"
		multiline: True
		text_size: self.width*0.98, None
		size_hint_x: 1.0
		size_hint_y: None
		height: self.texture_size[1] + 15
		text: root.data_label
		markup: True
		on_ref_press: root.linki()		



	TextInput:
		id: Inp
		multiline: False
		padding_y: (5,5)
		size_hint: (1, 0.5)
		on_text: app.process()

	Button:
		text: "Поиск по названию"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback()

	Button:
		text: "Поиск по описанию"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback2()

	Button:
		text: "Случайный"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback3()

	Button:
		text: "Отправить"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback4()

"""

KV_2 = """
MyBL:
	orientation: "vertical"
	size_hint: (0.95, 0.95)
	pos_hint: {"center_x": 0.5, "center_y":0.5}

	Label:
		font_size: "15sp"
		multiline: True
		background_color:'#00FFCE'
		text_size: self.width*0.98, None
		size_hint_x: 1.0
		size_hint_y: None
		height: self.texture_size[1] + 15
		text: root.data_label
		markup: True
		on_ref_press: root.linki()		


	Image:
		source: 'mylogo.png'

	Button:
		text: "Поиск по названию"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback()

	Button:
		text: "Поиск по описанию"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback2()

"""


class ScreenMain(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        button_new_pasword = Button(
            text="New Pasword",
            background_color=[0, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_new_pasword,
        )

        button_new = Button(
			text="Поиск по названию",
			background_color=[0, 1.5, 3, 1],
			size_hint=[1, 0.1],
			on_press=self._on_press_button_new_pasword,
		)

        img = Image(source='mylogo.png',)

        boxlayout.add_widget(img)
        boxlayout.add_widget(button_new)
        boxlayout.add_widget(button_new_pasword)
        self.add_widget(boxlayout)

    def _on_press_button_new_pasword(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'lenpasword'


class LenPasword(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        button_new_pasword = Button(
            text="Return",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_new_pasword,
        )

        boxlayout.add_widget(button_new_pasword)
        self.add_widget(boxlayout)

    def _on_press_button_new_pasword(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'


class PaswordingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='main_screen'))
        sm.add_widget(LenPasword(name='lenpasword'))

        return sm

if __name__ == "__main__":
    PaswordingApp().run()






