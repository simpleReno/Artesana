# Import KivyMD Modules
from kivymd.uix.screen import MDScreen
# Import Custom Modules
from pos_app.adapters.ui.gui.baseclass.widgets import NavigationRailItem
class InventoryWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Inventory'
    def switch_navigation_rail(self, screen_name):
        self.ids.screen_manager.current = screen_name
# Load Screen Classes
class ScreenProduct(MDScreen):
    pass
class ScreenCategory(MDScreen):
    pass
class ScreenService(MDScreen):
    pass
    
   
                
    
   