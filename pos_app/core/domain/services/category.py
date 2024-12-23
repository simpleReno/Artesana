
#Import ports
from pos_app.core.application.interfaces.service import ICategoryService
#Import models
from pos_app.core.domain.models.category import Category

class CategoryService(ICategoryService):
    def __init__(self, category_repository):
        self.category_repo = category_repository

    def create_category(self, category_name, category_type, parent_id):
        category = Category(category_name=category_name, category_type=category_type, parent_id=parent_id)
        self.category_repo.save(category)
        return category

    def get_category(self, category_id):
        return self.category_repo.get(category_id)

    def update_category(self, category_id, category):
        self.category_repo.update(category_id, category)

    def get_all_categories(self):
        return self.category_repo.get_all()

    def delete_category(self, category_id):
        self.category_repo.delete(category_id)