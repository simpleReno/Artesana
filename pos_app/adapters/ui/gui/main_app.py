import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.uix.behaviors import ButtonBehavior

class LoginWindow(Screen):
    
    def login(self):
        self.manager.current = 'main'
        
    def show_decimal_keyboard(self):
        popup = DecimalKeyboardPopup()
        b = Button(text='Ok', size_hint=(1, 1))
        popup.ids.keyboard_layout.add_widget(b)
        popup.open()

# class AuthWindow(Screen):
#     pass

class MainWindow(Screen):
    
    def populate_tabs(self):
        pass
            

# class OrdersWindow(Screen):
#     pass

# class AccountWindow(Screen):
#     pass

class DecimalKeyboardPopup(Popup):
    def on_button_click(self, button):
        self.ids.text_input.text += button.text
        
    def on_delete_button_click(self):
        self.ids.text_input.text = self.ids.text_input.text[:-1]
        

class Main_app(App):
    def build(self):
        
        Builder.load_file("main_window.kv")
        Builder.load_file("login_window.kv")
        Builder.load_file("decimal_keyboard_popup.kv")
        
        sm = ScreenManager()
        
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(MainWindow(name='main'))
        
        
        return sm
    
if __name__ == '__main__':
    Main_app().run()