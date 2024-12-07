# import Kivy Modules
from kivy.metrics import dp
from kivy.animation import Animation
# Import KivyMD Modules
from kivymd.uix.screen import MDScreen
from kivymd.uix.expansionpanel import MDExpansionPanel
# Import Baseclass
from pos_app.adapters.ui.gui.baseclass.widgets import TrailingPressedIconButton
class HomeWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # Reassign Grid Layout Columns
    def on_window_resize(self, *args):
        grid_products = self.ids.products.ids.related_content.children[0].children[0].children[0]
        new_cols = max(1, int(self.ids.products.ids.related_content.children[0].width / dp(130)))
        grid_products.cols = new_cols
        print(grid_products.cols)
    def switch_navigation_rail(self, screen_name):
        self.ids.screen_manager.current = screen_name
    def tap_expansion_chevron(
        self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton
    ):
        Animation(
            padding=[0, dp(12), 0, dp(12)]
            if not panel.is_open
            else [0, 0, 0, 0],
            d=0.2,
        ).start(panel)
        panel.open() if not panel.is_open else panel.close()
        panel.set_chevron_down(
            chevron
        ) if not panel.is_open else panel.set_chevron_up(chevron)
        
# Load Screen Classes
class ScreenProducts(MDScreen):
    pass
class ScreenTables(MDScreen):
    pass
class ScreenOrders(MDScreen):
    pass
class ScreenCharge(MDScreen):
    pass