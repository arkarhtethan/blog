from django.test import TestCase, Client
from django.urls import reverse, resolve
from post import views
from post.models import Post
from model_mommy import mommy
from pprint import pprint as pp
from utils.random_string_generator import random_string_generator
from utils.unique_slug_field_generator import unique_slug_generator


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

        self.url = reverse("post:detail", kwargs={"slug": self.model.slug})

        self.response = self.client.get(self.url)

    def test_page_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_template_use(self):

        self.assertTemplateUsed(self.response, 'post/post_detail.html')

    def test_view_func(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.PostDetailView)


class ContactPageStatusTestCaseView(TestCase):

    def setUp(self):

        self.client = Client()

        data = {
            "name": "kaung myat han",
            'email': "arkarhtethan@gmail.com",
            "comment": "hellow",
        }

        self.url = reverse("post:contact")

        self.response = self.client.get(self.url)

        self.post_response = self.client.post(self.url, data=data)

    def test_post_status_code(self):

        self.assertEqual(self.post_response.status_code, 200)

    def test_page_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_template_use(self):

        self.assertTemplateUsed(self.response, 'post/contact.html')

    def test_view_func(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.ContactView)


class SharePageStatusTestCaseView(TestCase):

    def setUp(self):

        self.client = Client()

        data = {
            "name": "kaung myat han",
            'email': "arkarhtethan@gmail.com",
            'to': "arkarhtethan@gmail.com",
            "comment": "hellow",
        }

        self.model = mommy.make("Post")

        self.url = reverse("post:share", kwargs={"pk": self.model.pk})

        self.response = self.client.get(self.url)

        self.post_response = self.client.post(self.url, data=data)

    def test_post_status_code(self):

        self.assertEqual(self.post_response.status_code, 200)

    def test_page_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_template_use(self):

        self.assertTemplateUsed(self.response, 'post/share_post.html')

    def test_view_func(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func, views.share_post_view)


class CommentPageStatusTestCaseView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = mommy.make("Post")

        self.url = reverse("post:add_comment", kwargs={
                           "slug": self.model.slug})

        self.response = self.client.get(self.url)

        data = {
            "name": "Kaung myat",
            'email': "ar@gmail.com",
            'body': "wtf"
        }

        self.post_response = self.client.post(self.url, data=data)

    def test_page_status_code(self):

        self.assertEqual(self.response.status_code, 302)

    def test_create_comment(self):

        self.assertEqual(self.post_response.status_code, 200)

    def test_view_func(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func, views.post_comment)


class SearchPageStatusTestCaseView(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("post:search")

        self.response = self.client.get(self.url)

        search_url = "".join([self.url, '?q=hello'])

        self.search_response = self.client.get(search_url)

    def test_page_status_with_search_query(self):

        self.assertEqual(self.search_response.status_code, 200)

    def test_page_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_view_func(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.SearchView)


class TestUtilFunction(TestCase):

    def setUp(self):
        pass

    def test_random_string_generator(self):

        string = random_string_generator()

        self.assertEqual(len(string), 10)

    def test_unique_slug_generator(self):

        post = mommy.make("Post")

        string = unique_slug_generator(post, post.slug)

        posts = Post.objects.filter(slug=post.slug)

        self.assertEqual(posts.count(), 1)

        self.assertNotEqual(string, post.slug)


class TestSearchTagView(TestCase):

    def setUp(self):

        self.url = reverse("post:search-tag")

        self.client = Client()

        self.response = self.client.get(self.url)

        model = mommy.make("Tag")

        search_url = "".join([self.url, f'?q={model.name}'])

        self.response_search = Client().get(search_url)

    def test_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_status_search_response_code(self):

        self.assertEqual(self.response_search.status_code, 200)

    def test_template_use(self):

        self.assertTemplateUsed(self.response, 'post/home.html')
