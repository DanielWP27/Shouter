from django.test import TestCase
from django.urls import resolve, reverse
from django.contrib.auth import authenticate, login, logout
from shoutsite.factories import UserFactory,  ShoutFactory
from django.http import HttpRequest
from django.conf import settings
from importlib import import_module
from django.contrib.auth.hashers import make_password
from shoutsite import views #from shoutsite.views import feed

class TestFeed(TestCase):

    #Tests that the feed url is correct
    def test_feed_url(self):
        url = resolve('/')
        self.assertEqual(url.func, views.feed)

    '''def test_feed_template(self):
        response = self.client.get(reverse(views.feed))
        self.assertTemplateUsed(self, response, 'shouts/feeds.html')'''

class TestProfile(TestCase):
    
    #Creates a user for test purposes
    def setUp(self):
        self.user = UserFactory(username='test')

    #Tests that the profile url is correct
    def test_profile_url(self):
        url = resolve('/profile/test')
        self.assertEqual(url.func, views.profile)

    #Tests that you have to be logged in to view this page
    def test_authentication_control(self):
        response = self.client.get(reverse('profile', kwargs={'username': 'first'}))
        self.assertEqual(response.status_code, 302)

        self.client.login(username='test', password='test')
        response = self.client.get(reverse('profile', kwargs={'username': 'first'}))
        self.assertEqual(response.status_code, 200)
        
    
class TestLoginUser(TestCase):
    def setUp(self):
        self.user = UserFactory(username='test')

    #Tests that the login url is correct
    def test_login_url(self):
        url = resolve('/login/')
        self.assertEqual(url.func, views.login_user)

    #Tests that you have to be logged in to view this page and that the redirection is correct
    def test_authentication_control_and_redirect(self):
        response = self.client.get(reverse('login_user'))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='test', password='test')
        response = self.client.get(reverse('login_user'))
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)

class TestLoginRedirect(TestCase):
    def setUp(self):
        self.user = UserFactory(username='test')

    #Tests that the feed url is correct  
    def test_login_redirect_url(self):
        url = resolve('/login_red/')
        self.assertEqual(url.func, views.login_redirect)

    #Tests that you have to be logged in to view this page and that the redirects work correctly
    def test_authentication_control_and_redirect(self):
        response = self.client.get(reverse('login_redirect'))
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

        self.client.login(username='test', password='test')
        response = self.client.get(reverse('login_redirect'))
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)

class TestSubmitPost(TestCase):
    def setUp(self):
        self.user = UserFactory(username='test')
        
    #Tests that the submit_post url is correct
    def test_submit_post_url(self):
        url = resolve('/submit_post/')
        self.assertEqual(url.func, views.submit_post)

    def test_authentication_control_and_redirect(self):
        response = self.client.post('/submit_post/', {'shout_text': 'TEST'})
        self.assertEqual(response.status_code, 302)

        self.client.login(username='test', password='test')
        response = self.client.post('/submit_post/', {'shout_text': 'TEST'})
        self.assertEqual(response.status_code, 302)
