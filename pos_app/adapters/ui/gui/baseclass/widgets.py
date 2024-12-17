# Import Kivy Modules
import asynckivy
from kivy.metrics import dp
from kivy.app import App
# Import Kivy Properties
from kivy.properties import StringProperty, NumericProperty, ListProperty, BooleanProperty
#Import Kivy Components
from kivy.uix.recycleview import RecycleView
from kivy.uix.behaviors import ButtonBehavior
# Import KivyMD Modules
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldLeadingIcon,
    MDTextFieldHintText,
    MDTextFieldHelperText,
    MDTextFieldTrailingIcon,
    MDTextFieldMaxLengthText,
)
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.list import MDListItemTrailingIcon
from kivymd.uix.button import MDButton
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
class TabContent(RecycleView):
    pass
# Load Item List Display
class ItemListDisplay(RecycleView):
    pass
# Load Item Sub Category
class SubCategoryItem(MDBoxLayout):
    position = NumericProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.adaptive_size = True
        self.padding = dp(5)
        self.spacing = dp(5)
        self.text_field = self.add_widget(self.create_text_field("Subcategory"))
        self.description_field = self.add_widget(self.create_text_field("Description"))
        self.box_buttons = self.add_widget(self.create_box_buttons())
        
    def create_text_field(self, hint_text):
        text_field = MDTextField(
            MDTextFieldHintText(
                text = hint_text
            ),
            mode="filled",
        )
        return text_field
    
    def create_box_buttons(self):
        box_buttons = MDBoxLayout(
                HBButton(
                    text="Delete",
                    icon="close",
                    on_release=self.remove_self
                ),
                orientation="horizontal",
                adaptive_size=True,
                padding=dp(5),
            )
        return box_buttons
    
    def remove_self(self, *args):
        if self.parent:
            app = App.get_running_app()
            app.root.ids.inventory.ids.screen_manager.current_screen.remove_subcategory(self)
            self.parent.remove_widget(self)
    
    def to_dict(self):
        return {
            "viewclass": "SubCategoryItem",
            "position": self.position,
        }
# load Item Group
class ItemGroup():
    position = NumericProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.adaptive_size = True
        self.spacing = dp(5)
        self.add_widget(
            MDTextField(
                MDTextFieldHintText(
                    text="Group"
                ),
                MDTextFieldTrailingIcon(
                    icon="information"
                ),
                id="text_field",
                mode="filled"
            )
        )
        self.add_widget(
            MDBoxLayout(
                HBButton(
                text="Remove",
                icon="minus",
                on_release= self.remove_self     
                ),
                orientation="horizontal",
                adaptive_size=True,
                spacing=dp(5),
                )
        )
            
    def remove_self(self, *args):
        if self.parent:
            app = App.get_running_app()
            app.root.ids.inventory.ids.screen_manager.current_screen.remove_subcategory(self)
            self.parent.remove_widget(self)
            
    def to_dict(self):
        return {
            "viewclass": "ItemGroup",
            "position": self.position,
        }
# Load Homebrew Button
class HBButton(MDButton):
    text = StringProperty()
    icon = StringProperty()
# Load Data Table
class DataTable(MDBoxLayout):
    pass

class CheckItem(MDBoxLayout):
    text = StringProperty()
    group = StringProperty()
    active = BooleanProperty()
    
class DecimalKeyboard(MDBoxLayout):
    
    def on_click(self, instance):
        self.ids.text_field.text += instance.text
    
    def on_backspace(self):
        self.ids.text_field.text = self.ids.text_field.text[:-1]