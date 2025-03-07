from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class PostModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password')

    def test_post_with_valid_keywords(self):
        post = Post(
            title='Valid Title',
            description='Valid description.',
            keywords='keyword1, keyword2, keyword3',
            url='http://example.com',
            author=self.user,
            ip_address='127.0.0.1'
        )
        try:
            post.save()
        except ValidationError:
            self.fail(
                'Błędny post!')

    def test_post_with_insufficient_keywords(self):
        post = Post(
            title='Title',
            description='Description.',
            keywords='keyword1, keyword2',
            url='http://example.com',
            author=self.user,
            ip_address='127.0.0.1'
        )
        with self.assertRaises(ValidationError):
            post.save()

    def test_post_with_title_in_keywords(self):
        post = Post(
            title='title',
            description='Description.',
            keywords='title, keyword2, keyword3',
            url='http://example.com',
            author=self.user,
            ip_address='127.0.0.1'
        )
        with self.assertRaises(ValidationError):
            post.save()

    def test_post_with_duplicate_keywords(self):
        post = Post(
            title='Title',
            description='Description.',
            keywords='keyword1, keyword1, keyword2, keyword3',
            url='http://example.com',
            author=self.user,
            ip_address='127.0.0.1'
        )
        post.save()
        self.assertEqual(post.keywords, 'keyword1, keyword2, keyword3')

    def test_post_with_title_matching_keywords(self):
        post = Post(
            title='keyword1',
            description='Description.',
            keywords='keyword1, keyword2, keyword3, keyword4',
            url='http://example.com',
            author=self.user,
            ip_address='127.0.0.1'
        )
        with self.assertRaises(ValidationError):
            post.save()

    def test_post_with_exactly_matching_title_and_keywords(self):
        post = Post(
            title='DokładnyTytuł1, DokładnyTytuł2, tytuł3',
            description='Opis.',
            keywords='DokładnyTytuł1, DokładnyTytuł2, tytuł3',
            url='http://example.com',
            author=self.user,
            ip_address='127.0.0.1'
        )
        with self.assertRaises(ValidationError):
            post.save()
