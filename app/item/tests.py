from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import MagicMock
from .forms import NewItemForm, EditItemForm
from .models import Item,Category


class ItemFormTests(TestCase):
    def setUp(self):
        # Create a category to use in tests
        self.category = Category.objects.create(name='Test Category')
        # Mock the Item model instance
        self.mock_item = MagicMock(spec=Item)

    def test_new_item_form_valid(self):
        form_data = {
            'category': self.category.id,  # Use the ID of the created category
            'name': 'New Item',
            'description': 'New Description',
            'price': '19.99',
        }
        file_data = {
            'image': ''
        }
        form = NewItemForm(data=form_data, files=file_data)
        if not form.is_valid():
            print("NewItemForm errors:", form.errors)
        self.assertTrue(form.is_valid())

    def test_edit_item_form_valid(self):
        form_data = {
            'name': 'Updated Item',
            'description': 'Updated Description',
            'price': '29.99',
            'image': ''
        }
        form = EditItemForm(data=form_data, files=form_data)
        self.assertTrue(form.is_valid())

    def test_new_item_form_invalid(self):
        # Test with missing required fields
        form_data = {}
        form = NewItemForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_edit_item_form_invalid(self):
        # Test with invalid data (e.g., empty name)
        form_data = {
            'name': '',
            'description': 'Updated Description',
            'price': '29.99',
        }
        form = EditItemForm(data=form_data)
        self.assertFalse(form.is_valid())
