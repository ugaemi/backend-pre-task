from rest_framework.test import APITestCase

from apps.users.models import User


class TestUserAPITestCase(APITestCase):
    def setUp(self):
        email = 'tester@test.com'
        password = 'testpassword'
        self.user = User.objects.create_user(
            email=email,
            password=password,
        )
        self.client.login(email=email, password=password)

    def tearDown(self):
        self.client.logout()
        self.user.delete()
