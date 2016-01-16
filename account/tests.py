from django.test import TestCase

from django.contrib.auth.models import User
from .models import Account

class AccountTestCase(TestCase):
    def setUp(self):
        pass

    def test_account_slugify(self):
        u = User.objects.create(username='test_account_slugifyфыв')
        a = Account.objects.create(user=u)
        self.assertEquals(a.slug, 'test_account_slugifyфыв')

        # u1 = User.objects.create(username='test_account_slugifyфыв', first_name='test_account_slugifyфыв')
        # a1 = Account.objects.create(user=u1)
        # self.assertRegexpMatches(a1.slug, r'test_account_slugifyфыв-[\d]+')