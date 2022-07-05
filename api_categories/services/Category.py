from api_categories.models import Category


class CategoryService:
    @classmethod
    def get_category_id_by_name(cls, category_name):
        try:
            category = Category.objects.get(name=category_name)
            if category:
                return category.id
        except Exception as ex:
            print("Category not found!!! ", ex)
