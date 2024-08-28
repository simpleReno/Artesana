import os
from dotenv import load_dotenv
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from kivy.metrics import dp

load_dotenv()

def show_popup(title, message):
        show = Popup(title=title,
                     content=Button(text=message, on_press=lambda instance: show.dismiss()), 
                     size_hint=(None, None), 
                     size=(dp(400),dp(400)))
        show.open()
class LoginWindow(Screen):
    
    def login(self):
        if self.ids.username_input.text == os.environ.get('USERNAME') and self.ids.password_input.text == os.environ.get('PASSWORD'):
            self.manager.current = 'pin'
            self.ids.username_input.text = ""
            self.ids.password_input.text = ""
        else:
            show_popup("Invalid Credentials", "OK")
            self.ids.username_input.text = ""
            self.ids.password_input.text = ""
        
    def show_decimal_keyboard(self):
        popup = DecimalKeyboardPopup()
        b = Button(text='Ok', size_hint=(1, 1))
        b.bind(on_press=lambda instance: (setattr(self.ids.password_input, 'text', popup.ids.text_input.text),popup.dismiss()))
        popup.ids.keyboard_layout.add_widget(b)
        popup.open()

class MainWindow(Screen):
    
    def populate_tabs(self):
        for i in range(1, 6):
            box = BoxLayout(orientation='vertical')
            label = Label(text=f'Drinks {i}')
            tab = TabbedPanelItem(text=f'Beers {i}')
            box.add_widget(label)
            tab.add_widget(box)
            self.ids.tabbed_panel.add_widget(tab)
            
            box2 = BoxLayout(orientation='vertical')
            label2 = Label(text=f'Table {i}')
            tab2 = TabbedPanelItem(text=f'Sections {i}')
            box.add_widget(label2)
            tab.add_widget(box2)
            self.ids.tabbed_panel2.add_widget(tab2)
            
        if self.ids.tabbed_panel.tab_list:
                self.ids.tabbed_panel.switch_to(self.ids.tabbed_panel.tab_list[0])
                
        if self.ids.tabbed_panel2.tab_list:
                self.ids.tabbed_panel2.switch_to(self.ids.tabbed_panel2.tab_list[0])
            
class MenuScreen(Screen):
    pass
class OrderScreen(Screen):
     pass

class AccountScreen(Screen):
    pass

class PinKeyboard(Screen):
    def on_button_click(self, button):
        self.ids.text_output.text += button.text
        
    def on_clear_all_button_click(self):
        self.ids.text_output.text = ""
    
    def on_delete_button_click(self):
        if self.ids.text_output.text:
            self.ids.text_output.text = self.ids.text_output.text[:-1]
            
    def on_go_back_button_click(self):
        self.manager.current = "login"
    
    def check_pin(self):
        pin = self.ids.text_output.text
        print(pin)
        print(os.environ.get('PIN'))
        if pin == os.environ.get('PIN'):
            self.manager.current = "main"
            self.ids.text_output.text = ""
        else: 
            show_popup("Invalid PIN", "OK")
            self.ids.text_output.text = ""
            
class DecimalKeyboardPopup(Popup):
    def on_button_click(self, button):
        self.ids.text_input.text += button.text
        
    def on_delete_button_click(self):
        self.ids.text_input.text = self.ids.text_input.text[:-1]
        

class Main_app(App):
    def build(self):
        
        Builder.load_file("login_window.kv")
        Builder.load_file("decimal_keyboard_popup.kv")
        Builder.load_file("pin_keyboard.kv")
        Builder.load_file("main_window.kv")
        
        sm = ScreenManager()
        
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(PinKeyboard(name='pin'))
        sm.add_widget(MainWindow(name='main'))
        
        return sm
    
if __name__ == '__main__':
    Main_app().run()