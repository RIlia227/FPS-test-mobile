import sys

from kivy.app import App
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.clock import mainthread
from kivy.core.clipboard import Clipboard as Cb
import threading
import socket
import requests


surname = ''


def get_pos(find):
    toponym_to_find = find
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        pass
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    delta = size(toponym)
    return toponym_longitude, toponym_lattitude, delta


def size(top):
    f = top["boundedBy"]["Envelope"]["lowerCorner"].split()
    f2 = top["boundedBy"]["Envelope"]["upperCorner"].split()
    x = abs(float(f[0]) - float(f2[0]))
    y = abs(float(f[1]) - float(f2[1]))
    return str(max(x, y))


def draw_map(arg1, arg2, number_type, delta, m_x, m_y):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={arg1},{arg2}&l={number_type}&spn={delta},{delta}&l=map&pt={m_x},{m_y},pm2rdl"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    return map_file


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
        global surname
        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        button_new_pasword = Button(
            text="Enter",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_new_pasword,
        )

        l = Label(text="Hello !",
                  font_size=50)

        self.Text_in = TextInput(font_size=50,
                      size_hint_y=None,
                      height=100)

        boxlayout.add_widget(l)
        boxlayout.add_widget(self.Text_in)
        boxlayout.add_widget(button_new_pasword)
        self.add_widget(boxlayout)

    def _on_press_button_new_pasword(self, *args):
        global surname
        surname = self.Text_in.text
        sm.add_widget(MapScreen(name='map_screen'))
        self.manager.transition.direction = 'left'
        self.manager.current = 'map_screen'


class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        if surname != "":
            x, y, delta = get_pos(surname)
            x, y, delta = float(x), float(y), float(delta)
            m_x, m_y = x, y

            img = Image(source=draw_map(x, y, types[number_type], delta, m_x, m_y), )

            boxlayout.add_widget(img)
        self.add_widget(boxlayout)


sm = ScreenManager()
sm.add_widget(ScreenMain(name='main_screen'))
sm.add_widget(LenPasword(name='lenpasword'))


class PaswordingApp(App):
    def build(self):
        return sm


number_type = 3
types = {1: "sat,skl",
         2: "sat",
         3: "map"
         }
if __name__ == "__main__":
    PaswordingApp().run()






