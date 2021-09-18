from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
# from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.properties import StringProperty,BooleanProperty
from kivy.metrics import dp
from kivy.uix.button import Button

class WidgetsExample(GridLayout):
    my_text=StringProperty("1")
    text_input=StringProperty("Ice cream")

    count=1
    flag=BooleanProperty(False)
    # slider_value_txt=StringProperty("0")
    def on_button_click(self):
        print("Button clicked")
        if self.flag:
            self.count+=1
            self.my_text=str(self.count)
    def on_switch_active(self,switch):
        print("Switch: "+str(switch.active))

    # def on_slider_value(self,slider):
        # self.slider_value_txt=str(int(slider.value))
        # print("Slider:"+str(int(slider.value)))
    def on_text_validate(self,widget):
        self.text_input=widget.text



    def on_toggle_button_state(self,toggle_button):

        print("toggle state "+toggle_button.state)
        if toggle_button.state=="down":
            toggle_button.text="ON"
            self.flag=True
        else:
            toggle_button.text="OFF"
            self.flag=False


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