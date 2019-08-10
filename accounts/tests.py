from django.test import TestCase

from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()


class UserTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username="adminteste", email="hello@cfe.com")
        user.set_password("testpassword")
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='adminteste')
        self.assertEqual(qs.count(), 1)


