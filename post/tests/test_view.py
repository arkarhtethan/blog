from django.test import TestCase, Client
from django.urls import reverse, resolve
from post import views

class HomePageStatusTestCaseView(TestCase):
    
    def setUp(self):

        self.client = Client()

        self.url = reverse("post:home")

        self.response = self.client.get(self.url)

    def test_page_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_template_use(self):

        self.assertTemplateUsed(self.response, 'post/home.html')

    def test_view_func(self):

        view_fun = resolve(reverse("post:home"))

        self.assertEqual(view_fun.func.view_class, views.BlogHome)

