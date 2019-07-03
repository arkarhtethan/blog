from django.test import TestCase, Client
from django.urls import reverse, resolve
from post import views
from post.models import Post
from model_mommy import mommy

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

class DetailPageTestCaseView(TestCase):
    
    def setUp(self):

        self.model = mommy.make("Post")

        self.client = Client()

        self.url = reverse("post:detail", kwargs={"slug":self.model.slug})

        self.response = self.client.get(self.url)

    def test_page_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_template_use(self):

        self.assertTemplateUsed(self.response, 'post/post_detail.html')

    def test_view_func(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.PostDetailView)

