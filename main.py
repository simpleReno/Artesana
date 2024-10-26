# Import Python Libraries
import os
from dotenv import load_dotenv
# Import Kivy
from kivy.core.window import Window 
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.scatter import Scatter
from kivy.weakproxy import WeakProxy
# Import Kivy Properties
from kivy.properties import StringProperty
# Import Kivy Components
from kivy.uix.scatter import Scatter
# Import KivyMD
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts_path
from kivymd.app import MDApp
# Import KivyMD Components
from kivymd.uix.list import MDListItem
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivymd.uix.navigationdrawer import MDNavigationDrawerItem
from kivymd.uix.card import MDCard
from kivymd.uix.recycleview import RecycleView
# Load Screen Classes
class ScreenHome(MDScreen):
    pass
class ScreenProfile(MDScreen):
    pass
class ScreenCart(MDScreen):
    pass
class ScreenHistory(MDScreen):
    pass
class ScreenLogout(MDScreen):
    pass
# Load Navigation Rail Items
class NavigationRailItem(MDNavigationRailItem):
    icon = StringProperty()
    text = StringProperty()
    screen = StringProperty()
# Load Navigation Drawer Items
class NavigationDrawerItem(MDNavigationDrawerItem):
    icon = StringProperty()
    text = StringProperty()
#Load Product Card
class ProductCard(MDCard):
    icon = StringProperty()
    text = StringProperty()
# Load Listed Items
class ListedItem(MDListItem):
    icon = StringProperty()
    text = StringProperty()
#Load Main Window
class RecycleViewLeft(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
class RecycleViewRight(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
class MainWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # Reassign Grid Layout Columns
    def on_window_resize(self, *args):
        grid_left = self.ids.home.ids.rv_l.children[0]
        new_cols = max(1, int(self.ids.home.width / dp(220)))
        grid_left.cols = new_cols

# Load Main App
class MainApp(MDApp):
    # init App
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Artesana"     
    # Build App
    def build(self):
        Window.bind(on_resize=self.on_window_resize)
        self.theme_cls.theme_styled_switch_animation = True
        self.theme_cls.theme_styled_switch_animation_duration = 0.2
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        return None
    # Set Theme Style
    def switch_theme_style(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"
        if self.theme_cls.primary_palette == "Blue":
            self.theme_cls.primary_palette = "Red"
        else:
            self.theme_cls.primary_palette = "Blue"
    # Switch Screen Function
    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
    # On Window Size
    def on_window_resize(self, *args):
        if self.root:
            self.root.on_window_resize()
    # On Start
    def on_start(self):
        self.root.ids.home.ids.rv_l.data.extend([
            {
                "viewclass": "ProductCard",
                "icon": "android",
                "text": "Product 1",
                "callback": lambda x: x,
            },
            {
                "viewclass": "ProductCard",
                "icon": "android",
                "text": "Product 2",
                "callback": lambda x: x,
            },
            {
                "viewclass": "ProductCard",
                "icon": "android",
                "text": "Product 3",
                "callback": lambda x: x,
            },
            {
                "viewclass": "ProductCard",
                "icon": "android",
                "text": "Product 4",
                "callback": lambda x: x,
            },
            {
                "viewclass": "ProductCard",
                "icon": "android",
                "text": "Product 5",
                "callback": lambda x: x,
            },
            {
                "viewclass": "ProductCard",
                "icon": "android",
                "text": "Product 6",
                "callback": lambda x: x,
            }
        ])
        self.root.ids.home.ids.rv_r.data.extend([
            {
                "viewclass": "ProductCard",
                "icon": "android",
                "text": "Product 1",
                "callback": lambda x: x,
            },
            {
                "viewclass": "ProductCard",
                "icon": "android",
                "text": "Product 2",
                "callback": lambda x: x,
            },
            {
                "viewclass": "ProductCard",
                "icon": "android",
                "text": "Product 3",
                "callback": lambda x: x,
            },
            {
                "viewclass": "ProductCard",
                "icon": "android",
                "text": "Product 4",
                "callback": lambda x: x,
            }
        ])
#  Run App   
if __name__ == "__main__":
    MainApp().run()