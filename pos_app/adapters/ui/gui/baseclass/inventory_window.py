# Import KivyMD Modules
from kivymd.uix.screen import MDScreen
# Import Custom Modules
from pos_app.adapters.ui.gui.baseclass.widgets import NavigationRailItem
class InventoryWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Inventory'
# Load Screen Classes
class ScreenProduct(MDScreen):
    pass
class ScreenCategory(MDScreen):
    pass
class ScreenService(MDScreen):
    pass
    
   
                
    
   