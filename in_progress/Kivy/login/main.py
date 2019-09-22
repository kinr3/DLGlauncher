from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.graphics import BorderImage
from kivy.graphics import Color, Rectangle
from kivy.uix.image import AsyncImage
import time, threading


from kivy.uix.progressbar import ProgressBar

Builder.load_string("""
<MenuScreen>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            source: 'image/LoginFenster.png'
            size: self.size

    FloatLayout:
        Button:
            background_color: 0.1,0.1,0.1,1
            pos_hint: {'x':0.5, 'y':0.1}
            size_hint: 0.1, 0.1
            text: 'Goto settings'
            on_press:
                root.pb()
                print('ho')
        Button:
            background_color: 0.1,0.1,0.1,1
            pos_hint: {'x':0.8, 'y':0.1}
            size_hint: 0.1, 0.1
            text: 'Quit'
            on_press:
                print('hi')
                root.manager.transition.direction = 'left'
                root.manager.current = 'settings'


<SettingsScreen>:
    FloatLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
""")


class PBarr(ProgressBar):
    value = 0

    def update(self):
        self.value += 1
        if self.value >= 100:
            app = App.get_running_app()
            Clock.unschedule(app.event)
            print('fin ')
            self.value = 0


class MenuScreen(Screen):

    def pb(self):
        p = PBarr()
        event = Clock.unschedule_interval(lambda dt: p.update(), 0.2)
        threading.Thread(target=event).start()



class SettingsScreen(Screen):
    pass





sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))


class MainApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    MainApp().run()