from django.test import TestCase
from model_mommy import mommy
from post.models import Post


class TestPostModel(TestCase):

    def setUp(self):

        self.model = mommy.make("Post")

    def test_instance(self):

        self.assertTrue(isinstance(self.model, Post))

    def test_str(self):

        self.assertEqual(str(self.model), self.model.title)

    def test_slug(self):

        self.assertTrue(len(self.model.slug) > 1)
