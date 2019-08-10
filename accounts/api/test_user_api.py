from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

User = get_user_model()


class UserTestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(username="adminteste", email="hello@cfe.com")
        user.set_password("testpassword")
        user.save()

    def test_created_user_std(self):
        qs = User.objects.filter(username='adminteste')
        self.assertEqual(qs.count(), 1)

    def test_register_user_api_fail(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'cfe.doe',
            'email': 'cfe.doe@gmail.com',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password2'][0], 'This field is required.')

    def test_register_user_api(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'cfe.doe',
            'email': 'cfe.doe@gmail.com',
            'password': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token_len = len(response.data.get("token", 0))
        self.assertGreater(token_len, 0)

    def test_login_user_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'adminteste',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get("token", 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertGreater(token_len, 0)

    def test_login_user_api_fail(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'admintestefailllll',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        token = response.data.get("token", 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertEqual(token_len, 0)

    def test_token_login_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'adminteste',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get("token", None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)

    def test_token_register_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'adminteste',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get("token", None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        url2 = api_reverse('api-auth:register')
        data2 = {
            'username': 'cfe.doe',
            'email': 'cfe.doe@gmail.com',
            'password': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(url2, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
