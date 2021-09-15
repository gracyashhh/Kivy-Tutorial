import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ChildApp(GridLayout):

    def __init__(self,**kwargs):
        super(ChildApp,self).__init__()
        self.cols=2
        self.add_widget(Label(text="Your Name please"))
        self.name=TextInput()
        self.add_widget(self.name)

        self.add_widget(Label(text="Your Age"))
        self.age = TextInput()
        self.add_widget(self.age)

        self.add_widget(Label(text="Crush Name"))
        self.crush_name = TextInput()
        self.add_widget(self.crush_name)

        self.submit = Button(text="Calculate Love")
        self.submit.bind(on_press=self.submit_data)
        self.add_widget(self.submit)
    def submit_data(self,instance):
        print("Name of the person:"+self.name.text)
        print("Name of the crush:"+self.crush_name.text)
        print("Age of the person:"+self.age.text)

class ParentApp(App):
    def build(self):
        return ChildApp()

if __name__=="__main__":
    ParentApp().run()