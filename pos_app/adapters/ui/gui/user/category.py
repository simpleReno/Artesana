#import ports
from pos_app.core.application.interfaces.user import ICategoryUser

class CategoryUser(ICategoryUser):
    def __init__(self, category_service):
        self.category_service = category_service
        
    def create_category(self, category_name, category_type, parent_id):
        return self.category_service.create_category(category_name, category_type, parent_id)
    
    def get_category(self, category_id):
        return self.category_service.get_category(category_id)
    
    def update_category(self, category_id, category):
        return self.category_service.update_category(category_id, category)
    
    def get_all_categories(self):
        return self.category_service.get_all_categories()