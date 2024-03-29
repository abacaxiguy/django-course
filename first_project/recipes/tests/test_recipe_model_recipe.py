from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name="Cat preparation_steps_is_html"),
            author=self.make_author(username="User preparation_steps_is_html"),
            title="Test title",
            description="Test description",
            slug="test_slug",
            preparation_time=10,
            preparation_time_unit="Minutes",
            servings=5,
            servings_unit="People",
            preparation_steps="Test preparation steps",
            cover="test.png"
        )

        recipe.full_clean()
        recipe.save()

        return recipe

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65)
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()

        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg="Recipe preparation_steps_is_html is not False"
        )

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()

        self.assertFalse(
            recipe.is_published,
            msg="Recipe is_published is not False"
        )

    def test_recipe_string_representation(self):
        test_title = "Testing Representation"
        self.recipe.title = test_title
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), test_title,
            msg=f"Recipe string representation must be "
                f"'{test_title}' but got {str(self.recipe)}.")
