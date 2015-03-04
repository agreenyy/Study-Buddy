from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.layout import Layout
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

Builder.load_file('studybuddy.kv')

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: "vertical"
        spacing: 10
        Button:
            text: "TIMETABLE"
            font_size: 30
            background_color: (1, 0.2, 0, 0.4)
            size_hint: 1, 1
            on_press: root.manager.current = "timetable"

        Button:
            text: "FINANCES"
            font_size: 30
            background_color: (0, 0, 1, 0.3)
            size_hint: 1, 1
            on_press: root.manager.current = "finances"

        Button:
            text: "DEADLINES"
            font_size: 30
            background_color: (0, 1, 0, 0.3)
            size_hint: 1, 1
            on_press: root.manager.current = "deadlines"

        Button:
            text: "HINTS AND TIPS"
            font_size: 30
            size_hint: 1, 1
            background_color: (1, 0, 0, 0.2)
            on_press: root.manager.current = "hints"

<TimetableScreen>:
    BoxLayout:
        orientation: "vertical"
        spacing: 20
        Button:
            text: "WEEK 1"
            font_size: 30
            size_hint: 1, 1
            on_press: root.manager.current = "one"

        Button:
            text: "WEEK 2"
            font_size: 30
            size_hint = 1, 1
            on_press: root.manager.current = "two"

        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = "menu"

<FinancesScreen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = "menu"

<DeadlinesScreen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = "menu"

<HintsScreen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = "menu"

<OneScreen>:
    BoxLayout:
        Button:
            text: "Back to Timetable"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = "timetable"

<TwoScreen>:
    BoxLayout:
        Button:
            text: "Back to Timetable"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = "timetable"


""")
class MenuScreen(Screen):
    pass

class TimetableScreen(Screen):
    pass

class FinancesScreen(Screen):
    pass

class DeadlinesScreen(Screen):
    pass

class HintsScreen(Screen):
    pass

class OneScreen(Screen):
    pass

class TwoScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name = "menu"))
sm.add_widget(TimetableScreen(name = "timetable"))
sm.add_widget(FinancesScreen(name = "finances"))
sm.add_widget(DeadlinesScreen(name = "deadlines"))
sm.add_widget(HintsScreen(name = "hints"))
sm.add_widget(OneScreen(name = "one"))
sm.add_widget(TwoScreen(name = "two"))

class StudyBuddyApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    StudyBuddyApp().run()
