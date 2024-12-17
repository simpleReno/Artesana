from sqlalchemy.orm import Session
from pos_app.core.domain.models.category import Category
from pos_app.core.application.interfaces.repository import ICategoryRepository

class CategoryRepository(ICategoryRepository):
    def __init__(self, session: Session):
        self.session = session
    def save(self, category: Category) -> None:
        try:
            category_entity = Category(
                id = category.id,
                name = category.name,
                description = category.description
            )
            self.session.add(category_entity)
            self.session.commit()
            self.session.refresh(category_entity)

        except Exception as e:
            raise e
        finally:
            self.session.close()

    def get(self, category_id: str):
        pass
    
    def update(self, category_id: str, order: Category):
        pass

    def get_all(self):
        pass
    
    def delete(self, category_id: str):
        pass