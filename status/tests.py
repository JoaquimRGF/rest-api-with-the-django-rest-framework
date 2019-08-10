from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Status
# Create your tests here.

User = get_user_model()


class StatusTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username="adminteste", email="hello@cfe.com")
        user.set_password("testpassword")
        user.save()

    def test_creating_status(self):
        user = User.objects.get(username='adminteste')
        obj = Status.objects.create(user=user, content="Some cool new content")
        self.assertEqual(obj.id, 1)
        qs = Status.objects.all()
        self.assertEqual(qs.count(), 1)


