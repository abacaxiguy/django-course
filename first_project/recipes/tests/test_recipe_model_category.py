from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeTestBase


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self):
        self.category = self.make_category()
        return super().setUp()

    @parameterized.expand([
        ('name', 65),
    ])
    def test_recipe_category_fields_max_length(self, field, max_length):
        setattr(self.category, field, 'A' * (max_length + 1))

        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_recipe_category_model_string_representation_is_name_field(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )
