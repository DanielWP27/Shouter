# pylint: disable=no-member

from django.test import TestCase
from shoutsite.models import Shout
from shoutsite.factories import ShoutFactory, UserFactory, ProfileFactory

class ShoutTest(TestCase):
    def setUp(self):
        self.shout1 = ShoutFactory()
        self.shout1.save()

    def tearDown(self):
        self.shout1.delete()

    def test_can_read_shout_text(self):
        self.assertEqual('TEXT', self.shout1.shout_text)

    def test_can_read_pub_date(self):
        self.assertEqual('2019-01-22 10:06:09.268029', self.shout1.pub_date)

    def test_can_read_user_username(self):
        self.shout1.user.username = 'TestUser'
        self.shout1.save()
        self.assertEqual('TestUser', self.shout1.user.username)

    def test_can_read_likes(self):
        self.assertEqual(0, self.shout1.likes)
        self.shout1.likes = 10000
        self.shout1.save()
        self.assertEqual(10000, self.shout1.likes)
        '''self.shout1.likes = ' '
        self.shout1.save()
        self.assertRaises(TypeError, ' ', self.shout1.likes)'''

class UserTest(TestCase):
    def setUp(self):
        self.user1 = UserFactory()
        self.user1.save()

    def tearDown(self):
        self.user1.delete()

    def test_can_read_first_and_last_name(self):
        self.assertEqual('first', self.user1.first_name)
        self.assertEqual('last', self.user1.last_name)

    def test_can_read_user_username(self):
        self.assertEqual('first', self.user1.username)

    def test_can_confirm_password_hashed(self):
        self.assertNotEqual('test', self.user1.password)

class ProfileTest(TestCase):
    def setUp(self):
        self.profile1 = ProfileFactory()
        self.profile1.save()

    def tearDown(self):
        self.profile1.delete()

    def test_can_read_owner(self):
        self.assertEqual('first', self.profile1.owner.first_name)
        self.assertEqual('last', self.profile1.owner.last_name)

    