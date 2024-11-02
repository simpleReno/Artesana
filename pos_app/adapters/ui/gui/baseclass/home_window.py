# import Kivy Modules
from kivy.metrics import dp
# Import KivyMD Modules
from kivymd.uix.screen import MDScreen

class HomeWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # Reassign Grid Layout Columns
    def on_window_resize(self, *args):
        grid_left = self.ids.products.ids.tab_content.children[0]
        new_cols = max(1, int(self.ids.products.width / dp(220)))
        grid_left.cols = new_cols
        
# Load Screen Classes
class ScreenProducts(MDScreen):
    pass
class ScreenTables(MDScreen):
    pass
class ScreenOrders(MDScreen):
    pass
class ScreenCharge(MDScreen):
    pass