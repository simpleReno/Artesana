# Import Kivy Properties
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
# Import KivyMD Modules
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
# Import Custom Modules
from pos_app.adapters.ui.gui.baseclass.widgets import NavigationRailItem, SubCategoryItem, ItemGroup

class InventoryWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Inventory'

    def switch_navigation_rail(self, screen_name):
        self.ids.screen_manager.current = screen_name
        
class ScreenProduct(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_items = [
            {
                "text": f"Item {i}",
                "on_release": lambda x=f"Item {i}": self.set_item(x),
            } for i in range(5)]
        self.menu = MDDropdownMenu(
            items=self.menu_items
        )
        
    def open_menu(self):
        if not self.menu.parent:
            self.menu.caller = self.ids.drop_text
            self.menu.open()
            
    def set_item(self, text_item):
        self.ids.drop_text.text = text_item
        self.menu.dismiss()
class ScreenCategory(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def add_subcategory(self):
        self.ids.list.data.append(
            {
                "viewclass": "SubCategoryItem",
                "position": len(self.ids.list.data),
            }
        )
        
    def remove_subcategory(self, instance):
        try:
            obj = instance.to_dict()
            print(obj["position"])
            self.ids.list.data.remove(obj)
            for i, obj in enumerate(self.ids.list.data):
                obj["position"] = i
        except ValueError as e:
            print("Error:", e)  # Debugging statement
class ScreenService(MDScreen):
    pass
    
   
                
    
   