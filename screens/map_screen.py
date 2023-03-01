import sys

import requests
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


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
    print(arg1, arg2)
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={arg1},{arg2}&l={number_type}" \
                  f"&spn=0.095,0.095&pt=39.591378,52.601656,pm2gnl~39.601349,52.603532,pm2gnl~39.435455,52.609682,pm2gnl" \
                  f"~39.553370,52.563424,pm2gnl~39.615803,52.643330,pm2gnl"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "data/map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    return map_file


class MapScreen_Lipetsk(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        boxlayout = BoxLayout(orientation="vertical", spacing=10, padding=[0])
        x, y, delta = get_pos("Липецк")
        x, y, delta = float(x), float(y), float(delta)
        m_x, m_y = x, y
        img = Image(source=draw_map(x, y, "map", delta, m_x, m_y), )

        button_pay_1 = Button(
            text="Коммунальная площадь",
            background_color=[0, 0, 0, 0],
            size_hint=[1, 0.12],
            on_press=self._on_press_button_1,
        )

        button_pay_2 = Button(
            text="Октябрьский округ",
            background_color=[0, 0, 0, 0],
            size_hint=[1, 0.12],
            on_press=self._on_press_button_2,
        )

        button_pay_3 = Button(
            text="Косырёвское кладбище",
            background_color=[0, 0, 0, 0],
            size_hint=[1, 0.12],
            on_press=self._on_press_button_3,
        )

        button_pay_4 = Button(
            text="Студеновский карьер",
            background_color=[0, 0, 0, 0],
            size_hint=[1, 0.12],
            on_press=self._on_press_button_4,
        )

        button_pay_5 = Button(
            text="площадь Петра Великого",
            background_color=[0, 0, 0, 0],
            size_hint=[1, 0.12],
            on_press=self._on_press_button_5,
        )

        button_back = Button(
            background_normal='data/назад.png',
            size_hint=[1, 0.22],
            on_press=self._on_press_button_back,
            border=(0, 0, 0, 0)
        )

        boxlayout.add_widget(img)
        boxlayout.add_widget(button_pay_1)
        boxlayout.add_widget(button_pay_2)
        boxlayout.add_widget(button_pay_3)
        boxlayout.add_widget(button_pay_4)
        boxlayout.add_widget(button_pay_5)
        boxlayout.add_widget(button_back)
        self.add_widget(boxlayout)

    def _on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'

    def _on_press_button_1(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'parcing_screen_1'

    def _on_press_button_2(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'parcing_screen_2'

    def _on_press_button_3(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'parcing_screen_3'

    def _on_press_button_4(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'parcing_screen_4'

    def _on_press_button_5(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'parcing_screen_5'
