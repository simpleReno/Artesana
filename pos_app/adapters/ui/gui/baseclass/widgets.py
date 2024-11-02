# Import Kivy Modules
from kivy.metrics import dp
# Import Kivy Properties
from kivy.properties import StringProperty
#Import Kivy Components
from kivy.uix.recycleview import RecycleView
# Import KivyMD Modules
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDListItem
from kivymd.uix.navigationdrawer import MDNavigationDrawerItem
from kivymd.uix.navigationrail import MDNavigationRailItem

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(parent=self.update_width)
    def update_width(self, *args):
        if self.parent:
            self.width = self.parent.width
# Load Tab Content Recycle View
class TabContentRecycleView(RecycleView):
    pass
# Load Item List Display
class ItemListDisplay(RecycleView):
    pass