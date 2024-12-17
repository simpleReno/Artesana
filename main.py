# Import Python Libraries
from dotenv import load_dotenv
# Import Purge Cache Function
from pos_app.purge_pycache import delete_pycache
delete_pycache()  # Call this function at the start of your script
# Import Kivy
from kivy.core.window import Window 
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.weakproxy import WeakProxy
# Import Kivy Properties
from kivy.properties import StringProperty
from kivy.properties import ListProperty
# Import Kivy Components
from kivy.uix.scatter import Scatter
# Import KivyMD
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts_path
from kivymd.app import MDApp
# Import KivyMD Components
from kivymd.uix.list import MDListItem
from kivymd.uix.tab import MDTabsItem, MDTabsItemIcon, MDTabsItemText
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivymd.uix.navigationdrawer import MDNavigationDrawerItem
from kivymd.uix.card import MDCard
from kivymd.uix.recycleview import RecycleView
# Import baseclass
from pos_app.adapters.ui.gui.baseclass.widgets import ProductCard, TabContent
from pos_app.adapters.ui.gui.baseclass.home_window import HomeWindow
from pos_app.adapters.ui.gui.baseclass.clock_window import ClockWindow
from pos_app.adapters.ui.gui.baseclass.reports_window import ReportsWindow
from pos_app.adapters.ui.gui.baseclass.inventory_window import InventoryWindow
from pos_app.adapters.ui.gui.baseclass.settings_window import SettingsWindow
from pos_app.adapters.ui.gui.baseclass.management_window import ManagementWindow
from pos_app.adapters.ui.gui.baseclass.payroll_window import PayrollWindow
# Import Ports and Adapters
from pos_app.adapters.database.psql_adapter.connection import get_session
from pos_app.adapters.database.psql_adapter.repositories.order import OrderRepository
from pos_app.core.domain.services.order import OrderService
# Load Main App
class MainApp(MDApp):
    # init App
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Artesana"
    # Build App
    def build(self):
        # Window.bind(on_resize=self.on_window_resize)
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
    # Get Session
    # Switch Screen Function
    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
    # Switch Navigation Drawer Function
    def switch_navigation_drawer(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
        
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        if instance_tab:
            instance_tab.ids.tab_content.refresh_from_data()
    # On Start
    def on_start(self):
        # Getting widgets using ids
        tabs_home = self.root.ids.home.ids.products.ids.tabs
        home_content = self.root.ids.home.ids.products.ids.related_content
        list = self.root.ids.home.ids.products.ids.list
        # Add content to the tabs
        for category in ["Category 1", "Category 2", "Category 3", "Category 4"]:
            tab = MDTabsItem(
                MDTabsItemIcon(icon="beer"),
                MDTabsItemText(text=category),
            )
            tabs_home.add_widget(tab)
            tab_content = TabContent()
            tab_content.data.extend(
                [
                    {
                        "viewclass": "ProductCard",
                        "icon": "beer",
                        "text": "Product 1",
                        "callback": lambda x: x,
                    },
                    {
                        "viewclass": "ProductCard",
                        "icon": "beer",
                        "text": "Product 2",
                        "callback": lambda x: x,
                    },
                    {
                        "viewclass": "ProductCard",
                        "icon": "beer",
                        "text": "Product 3",
                        "callback": lambda x: x,
                    },
                    {
                        "viewclass": "ProductCard",
                        "icon": "beer",
                        "text": "Product 4",
                        "callback": lambda x: x,
                    },
                    {
                        "viewclass": "ProductCard",
                        "icon": "beer",
                        "text": "Product 5",
                        "callback": lambda x: x,
                    },
                    {
                        "viewclass": "ProductCard",
                        "icon": "beer",
                        "text": "Product 6",
                        "callback": lambda x: x,
                    },
                ]
            )
            home_content.add_widget(tab_content)
        # Test Data
        list.data.extend(
            [
                {
                    "viewclass": "ProductCard",
                    "icon": "beer",
                    "text": "Product 1",
                    "callback": lambda x: x,
                },
                {
                    "viewclass": "ProductCard",
                    "icon": "beer",
                    "text": "Product 2",
                    "callback": lambda x: x,
                },
                {
                    "viewclass": "ProductCard",
                    "icon": "beer",
                    "text": "Product 3",
                    "callback": lambda x: x,
                },
                {
                    "viewclass": "ProductCard",
                    "icon": "beer",
                    "text": "Product 4",
                    "callback": lambda x: x,
                },
            ]
        )
#  Run App   
if __name__ == "__main__":
    
    Session = get_session()
    
    order_repository = OrderRepository(Session)
    order_service = OrderService(order_repository)
    
    
    MainApp().run()