# Import KivyMD Modules
from kivymd.uix.screen import MDScreen

class ManagementWindow(MDScreen):
    
    def switch_navigation_rail(self, screen_name):
        self.ids.screen_manager.current = screen_name
class ScreenTables(MDScreen):
     pass
class ScreenAccounts(MDScreen):
     pass
class ScreenPromotions(MDScreen):
     pass
class ScreenDevolutions(MDScreen):
     pass
