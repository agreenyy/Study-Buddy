from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.layout import Layout
from kivy.core.window import Window
from kivy.uix.label import Label

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
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "timetable"

        Button:
            text: "FINANCES"
            font_size: 30
            background_color: (0, 0, 1, 0.3)
            size_hint: 1, 1
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "finances"

        Button:
            text: "DEADLINES"
            font_size: 30
            background_color: (0, 1, 0, 0.3)
            size_hint: 1, 1
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "deadlines"

        Button:
            text: "HINTS AND TIPS"
            font_size: 30
            size_hint: 1, 1
            background_color: (1, 0, 0, 0.2)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "hints"

<TimetableScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Week 1"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "week1"
        Button:
            text: "Week 2"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "week1"
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Week1Screen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Monday"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "monday1"
        Button:
            text: "Tuesday"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "tuesday1"
        Button:
            text: "Wednesday"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "wednesday1"
        Button:
            text: "Thursday"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "thursday1"
        Button:
            text: "Friday"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "friday1"
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Week2Screen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Monday"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "monday2"
        Button:
            text: "Tuesday"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "tuesday2"
        Button:
            text: "Wednesday"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "wednesday2"
        Button:
            text: "Thursday"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "thursday2"
        Button:
            text: "Friday"
            font_size: 30
            on_press:
                root.manager.transition.direction = "left"
                root.manager.current = "friday2"
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Monday1Screen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Tuesday1Screen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Wednesday1Screen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Thursday1Screen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Friday1Screen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Monday2Screen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Tuesday2Screen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Wednesday2Screen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Thursday2Screen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<Friday2Screen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<FinancesScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Budget Calculator"
            font_size: 30
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = "budgetcalculator"
        Button:
            text: "Spending Tracker"
            font_size: 30
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = "spendingtracker"
        Button:
            text: "Shopping List Creator"
            font_size: 30
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = "shoppinglist"
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<BudgetCalculatorScreen>:
    Button:
        text: "Back to Menu"
        height: "40dp"
        size_hint_y: None
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = "menu"

<SpendingTrackerScreen>:
    Button:
        text: "Back to Menu"
        height: "40dp"
        size_hint_y: None
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = "menu"

<ShoppingListScreen>:
    Button:
        text: "Back to Menu"
        height: "40dp"
        size_hint_y: None
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = "menu"

<DeadlinesScreen>:
    BoxLayout:
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

<HintsScreen>:
    BoxLayout:
        Button:
            text: "Housing Advice"
        Button:
            text: "Back to Menu"
            height: "40dp"
            size_hint_y: None
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"

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

class Week1Screen(Screen):
    pass

class Week2Screen(Screen):
    pass

class Monday1Screen(Screen):
    pass

class Tuesday1Screen(Screen):
    pass

class Wednesday1Screen(Screen):
    pass

class Thursday1Screen(Screen):
    pass

class Friday1Screen(Screen):
    pass

class Monday2Screen(Screen):
    pass

class Tuesday2Screen(Screen):
    pass

class Wednesday2Screen(Screen):
    pass

class Thursday2Screen(Screen):
    pass

class Friday2Screen(Screen):
    pass

class BudgetCalculatorScreen(Screen):
    pass

class SpendingTrackerScreen(Screen):
    pass

class ShoppingListScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name = "menu"))
sm.add_widget(TimetableScreen(name = "timetable"))
sm.add_widget(FinancesScreen(name = "finances"))
sm.add_widget(DeadlinesScreen(name = "deadlines"))
sm.add_widget(HintsScreen(name = "hints"))
sm.add_widget(Week1Screen(name = "week1"))
sm.add_widget(Week2Screen(name = "week2"))
sm.add_widget(Monday1Screen(name = "monday1"))
sm.add_widget(Tuesday1Screen(name = "tuesday1"))
sm.add_widget(Wednesday1Screen(name = "wednesday1"))
sm.add_widget(Thursday1Screen(name = "thursday1"))
sm.add_widget(Friday1Screen(name = "thursday1"))
sm.add_widget(Monday2Screen(name = "monday2"))
sm.add_widget(Tuesday2Screen(name = "tuesday2"))
sm.add_widget(Wednesday2Screen(name = "wednesday2"))
sm.add_widget(Thursday2Screen(name = "thursday2"))
sm.add_widget(Friday2Screen(name = "friday2"))
sm.add_widget(BudgetCalculatorScreen(name = "budgetcalculator"))
sm.add_widget(SpendingTrackerScreen(name = "spendingtracker"))
sm.add_widget(ShoppingListScreen(name = "shoppinglist"))
class StudyBuddyApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    StudyBuddyApp().run()
