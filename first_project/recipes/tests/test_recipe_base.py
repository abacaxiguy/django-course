from django.test import TestCase

from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def make_category(self, name="Test Category"):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name="Test",
        last_name="User",
        username="testuser",
        password="123456",
        email="test@email.com"
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
        self,
        category=None,
        author=None,
        title="Test Recipe",
        description="Test Description",
        slug="test-recipe",
        preparation_time=10,
        preparation_time_unit="minutes",
        servings=2,
        servings_unit="people",
        preparation_steps="Test Preparation Steps",
        preparation_steps_is_html=False,
        is_published=True,
        cover="test.jpg"
    ):
        category = self.make_category() if category is None else category
        author = self.make_author() if author is None else author

        return Recipe.objects.create(
            category=category,
            author=author,
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover=cover,
        )
