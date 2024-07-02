from django.test import TestCase
from .forms import ConversationMessageForm
from .models import ConversationMessage

class ConversationMessageFormTests(TestCase):

    def test_conversation_message_form_valid(self):
        form_data = {
            'content': 'This is a test message.'
        }
        form = ConversationMessageForm(data=form_data)
        if not form.is_valid():
            print("ConversationMessageForm errors:", form.errors)
        self.assertTrue(form.is_valid())

    def test_conversation_message_form_invalid(self):
        # Test with empty content, which should be invalid
        form_data = {
            'content': ''
        }
        form = ConversationMessageForm(data=form_data)
        if form.is_valid():
            print("ConversationMessageForm should be invalid but passed:", form.cleaned_data)
        self.assertFalse(form.is_valid())
