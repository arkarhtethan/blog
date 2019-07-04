from django.test import TestCase, Client
from django.urls import reverse, resolve
from post.forms import CommentForm, ContactForm, ShareForm
from model_mommy import mommy
from post import views


class TestCommentForm(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = mommy.make("Post")

        self.url = reverse("post:detail", kwargs={"slug": self.model.slug})

        self.response = self.client.get(self.url)

    def test_signup_page_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_csrf(self):

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_post_detail_template_use(self):

        self.assertTemplateUsed(self.response, 'post/post_detail.html')

    def test_comment_post_view(self):

        view = resolve(self.url)

        self.assertEqual(view.func.view_class, views.PostDetailView)

    def test_form_inputs_count(self):

        self.assertContains(self.response, '<input', 4)

    def test_name_input(self):

        self.assertContains(self.response, 'type="text"', 1)

    def test_form_csrf(self):

        self.assertContains(self.response, 'type="hidden"', 1)

    def test_email_input(self):

        self.assertContains(self.response, 'type="email"', 1)

    def test_submit_button(self):

        self.assertContains(self.response, 'type="submit"', 2)


class TestContactForm(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = mommy.make("Post")

        self.url = reverse("post:contact")

        self.response = self.client.get(self.url)

    def test_contact_page_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_csrf(self):

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_template_use(self):

        self.assertTemplateUsed(self.response, 'post/contact.html')

    def test_form_inputs_count(self):

        self.assertContains(self.response, '<input', 4)

    def test_name_input(self):

        self.assertContains(self.response, 'type="text"', 1)

    def test_form_csrf(self):

        self.assertContains(self.response, 'type="hidden"', 1)

    def test_email_input(self):

        self.assertContains(self.response, 'type="email"', 1)

    def test_submit_button(self):

        self.assertContains(self.response, 'type="submit"', 1)


class TestShareForm(TestCase):
    
    def setUp(self):

        self.client = Client()

        self.model = mommy.make("Post")

        self.url = reverse("post:share",kwargs={"pk":self.model.pk})

        self.response = self.client.get(self.url)

    def test_csrf(self):

        self.assertContains(self.response, 'csrfmiddlewaretoken')


    def test_form_inputs_count(self):

        self.assertContains(self.response, '<input', 6)

    def test_name_input(self):

        self.assertContains(self.response, 'type="text"', 2)

    def test_form_csrf(self):

        self.assertContains(self.response, 'type="hidden"', 1)

    def test_email_input(self):

        self.assertContains(self.response, 'type="email"', 2)

    def test_submit_button(self):

        self.assertContains(self.response, 'type="submit"', 2)
