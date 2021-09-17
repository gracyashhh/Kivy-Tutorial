from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
# from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivy.uix.button import Button

class WidgetsExample(GridLayout):
    my_text=StringProperty("1")
    count=1
    def on_button_click(self):
        print("Button clicked")
        self.count+=1
        self.my_text=str(self.count)

# class ScrollViewExample(ScrollView):
#     pass

class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # orientation with code
        self.orientation="lr-bt"

        # Responsive buttons
        # for i in range(1,11):
        #     b=Button(text=str(i),size_hint=(.2,.2))
        #     self.add_widget(b)
        # Fixed Size buttons
        for i in range(1,101):
            c=Button(text=str(i),size_hint=(None,None),size=(dp(100), dp(100)))
            self.add_widget(c)
        # Experimenting on random sizing
        # for i in range(1,11):
        #     size= dp(100) + i * 10
        #     c=Button(text=str(i),size_hint=(None,None),size=(size, size))
        #     self.add_widget(c)

class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    # def __init__(self,**kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation="vertical"
    #     b1=Button(text="A")
    #     b2=Button(text="B")
    #     b3=Button(text="C")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()