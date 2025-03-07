from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from management.models import Post
from rest_framework_simplejwt.tokens import RefreshToken


class PostAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))

    def test_create_post(self):
        url = reverse('post-list')
        data = {
            'title': 'Mój pierwszy post',
            'description': 'Opis mojego pierwszego posta.',
            'keywords': 'keyword1, keyword2, keyword3',
            'url': 'http://example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Mój pierwszy post')

    def test_update_post(self):
        post = Post.objects.create(
            title='Mój pierwszy post',
            description='Opis mojego pierwszego posta.',
            keywords='keyword1, keyword2, keyword3',
            url='http://example.com',
            author=self.user,
            ip_address='127.0.0.1'
        )
        url = reverse('post-detail', kwargs={'pk': post.pk})
        data = {
            'title': 'Zaktualizowany tytuł',
            'description': 'Zaktualizowany opis.',
            'keywords': 'keyword1, keyword2, keyword3',
            'url': 'http://example.com'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, 'Zaktualizowany tytuł')

    def test_delete_post(self):
        post = Post.objects.create(
            title='Mój pierwszy post',
            description='Opis mojego pierwszego posta.',
            keywords='keyword1, keyword2, keyword3',
            url='http://example.com',
            author=self.user,
            ip_address='127.0.0.1'
        )
        url = reverse('post-detail', kwargs={'pk': post.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
