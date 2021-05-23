from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status


class ContactsViewSetTests(APITestCase):
    """
    Tests of ContactsViewSet in contacts.presenters.views.contacts.py
    """

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.user.is_active = True
        self.user.save()

        response = self.client.post('/auth/token/obtain/', {'username': self.username, 'password': self.password},
                                    format='json')

        self.token = response['token']

        self.data: dict = {
            "name": "john34",
            "phoneNumber": "8598989899"
        }

    def test_get_with_param(self):
        response = self.client.get('/contacts/1/search', HTTP_AUTHORIZATION="JWT " + self.token)
        self.assertEqual(response.status_code, 200)

    def test_get_without_param(self):
        response = self.client.get('/contacts', HTTP_AUTHORIZATION="Token "+ self.token.key)
        self.assertEqual(response.status_code, 200)

    def test_post_with_data(self):
        self.client.force_login(user=self.user)
        response = self.client.post('/contacts', data=self.data, format="json", HTTP_AUTHORIZATION="Token "+ self.token.key)
        self.assertEqual(response.status_code, 200)

    def test_post_without_data(self):
        self.client.force_login(user=self.user)
        response = self.client.post('/contacts', data={}, format="json", HTTP_AUTHORIZATION="Token "+ self.token.key)
        self.assertEqual(response.status_code, 200)

    def test_update_with_data(self):
        self.client.force_login(user=self.user)
        response = self.client.put('/contacts/1/update', data=self.data, format="json", HTTP_AUTHORIZATION="Token "+ self.token.key)
        self.assertEqual(response.status_code, 200)

    def test_update_without_data(self):
        self.client.force_login(user=self.user)
        response = self.client.put('/contacts/1/update', data={}, format="json", HTTP_AUTHORIZATION="Token "+ self.token.key)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.client.force_login(user=self.user)
        response = self.client.delete('/contacts/1/delete', HTTP_AUTHORIZATION="Token "+ self.token.key)
        self.assertEqual(response.status_code, 200)


class UserApiAuthTestCase(APITestCase):
    """
    Tests of all controllers of JWT Auth in contacts.presenters.views.auth.py
    """

    def setUp(self):
        self.username = "test"
        self.email = "testn@test.com"
        self.password = "Test123@"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = ''

    def test_api_jwt(self):
        self.user.is_active = False
        self.user.save()

        response = self.client.post('/users/token/obtain/', {'username': self.username, 'password': self.password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.user.is_active = True
        self.user.save()

        response = self.client.post('/users/token/obtain/', {'username': self.username, 'password': self.password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
