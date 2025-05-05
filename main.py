# Import Purge Cache Function
from pos_app.purge_pycache import delete_pycache
delete_pycache()  # Call this function at the start of your script
# Import KivyMD APP
from kivymd.app import MDApp
# Import KivyMD Components
from kivymd.uix.tab import MDTabsItem, MDTabsItemIcon, MDTabsItemText
# Import baseclass
from pos_app.adapters.ui.gui.baseclass.widgets import TabContent

# Import Ports and Adapters
from pos_app.adapters.database.psql_adapter.connection import get_session, get_engine
from pos_app.adapters.database.psql_adapter.repositories.order import OrderRepository
from pos_app.core.domain.services.order import OrderService
from pos_app.adapters.ui.gui.user.order import OrderUser
from pos_app.adapters.database.psql_adapter.repositories.category import CategoryRepository
from pos_app.core.domain.services.category import CategoryService
from pos_app.adapters.ui.gui.user.category import CategoryUser
#Import Base database
from pos_app.core.domain.models.base import metadata
from pos_app.core.domain.models.customer import Customer
from pos_app.core.domain.models.order import Order
from pos_app.core.domain.models.payment import Payment
from pos_app.core.domain.models.product import Product
from pos_app.core.domain.models.table import Table
from pos_app.core.domain.models.delivery import Delivery
from pos_app.core.domain.models.order_detail import OrderDetail
from pos_app.core.domain.models.category import Category
# Import windows
from pos_app.adapters.ui.gui.baseclass.home_window import HomeWindow
from pos_app.adapters.ui.gui.baseclass.inventory_window import InventoryWindow
# Load Main App
class MainApp(MDApp):
    # init App
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Artesana"
    # Build App
    def build(self):
        self.theme_cls.theme_styled_switch_animation = True
        self.theme_cls.theme_styled_switch_animation_duration = 0.2
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        
        # order_repository = OrderRepository(get_session())
        # order_service = OrderService(order_repository)
        # order_user = OrderUser(order_service)
        # category_repository = CategoryRepository(get_session())
        # category_service = CategoryService(category_repository)
        # category_user = CategoryUser(category_service)
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

    # Engine = get_engine()
    # metadata.create_all(Engine, tables=[Category.__table__,
    #                                     Delivery.__table__,
    #                                     Customer.__table__,
    #                                     Order.__table__,
    #                                     Payment.__table__,
    #                                     Product.__table__,
    #                                     Table.__table__,
    #                                     OrderDetail.__table__])

    
    MainApp().run()