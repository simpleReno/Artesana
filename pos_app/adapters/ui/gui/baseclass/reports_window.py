# Import KivyMD Modules
from kivymd.uix.screen import MDScreen

class ReportsWindow(MDScreen):
    
    def switch_navigation_rail(self, screen_name):
        self.ids.screen_manager.current = screen_name
        
class ScreenReports_Total(MDScreen):
    pass
class ScreenReports_Products(MDScreen):
    pass
class ScreenReports_Services(MDScreen):
    pass