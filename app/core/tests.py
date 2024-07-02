from django.test import TestCase
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm


class FormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='strongpassword123')

    def test_signup_form_valid(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newstrongpassword123',
            'password2': 'newstrongpassword123',
        }
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_email(self):
        form_data = {
            'username': 'newuser',
            'email': 'invalid-email',
            'password1': 'newstrongpassword123',
            'password2': 'newstrongpassword123',
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_signup_form_password_mismatch(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newstrongpassword123',
            'password2': 'differentpassword123',
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_login_form_valid(self):
        form_data = {
            'username': 'testuser',
            'password': 'strongpassword123',
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid_username(self):
        form_data = {
            'username': 'wronguser',
            'password': 'strongpassword123',
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)

    def test_login_form_invalid_password(self):
        form_data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)
