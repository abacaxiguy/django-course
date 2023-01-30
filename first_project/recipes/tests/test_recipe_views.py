from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn('No recipes found here 😖', content)

    def test_recipe_home_template_loads_recipes(self):
        testing_title = "This tests for home template loads recipes"
        self.make_recipe(title=testing_title)

        response = self.client.get(reverse('recipes:home'))
        response_recipes = response.context['recipes']
        content = response.content.decode('utf-8')

        self.assertIn(testing_title, content)
        self.assertEqual(len(response_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        testing_title = "This tests for recipes that aren't published"
        self.make_recipe(title=testing_title, is_published=False)

        response = self.client.get(reverse('recipes:home'))
        response_recipes = response.context['recipes']
        content = response.content.decode('utf-8')

        self.assertIn('No recipes found here 😖', content)
        self.assertEqual(len(response_recipes), 0)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={"category_id": 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_status_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={"category_id": 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        testing_title = "This tests for category template"
        self.make_recipe(title=testing_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(testing_title, content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        testing_title = "This tests for recipes that aren't published"
        recipe = self.make_recipe(title=testing_title, is_published=False)

        response = self.client.get(
            reverse('recipes:category', kwargs={
                    "category_id": recipe.category.id})
        )

        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={"id": 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_status_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={"id": 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        testing_title = "This tests for detail template"
        self.make_recipe(title=testing_title)

        response = self.client.get(reverse('recipes:recipe', kwargs={"id": 1}))
        content = response.content.decode('utf-8')

        self.assertIn(testing_title, content)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        testing_title = "This tests for a recipe that isn't published"
        recipe = self.make_recipe(title=testing_title, is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={"id": recipe.id}))

        self.assertEqual(response.status_code, 404)

    def test_recipe_search_view_function_is_correct(self):
        view = resolve(reverse('recipes:search'))

        self.assertIs(view.func, views.search)

    def test_recipe_search_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
