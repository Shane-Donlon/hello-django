from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    def test_item_name_required(self):
        form = ItemForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_not_required(self):
        form = ItemForm({"name": "Testing Item ToDo"})
        self.assertTrue(form.is_valid())

    def test_explicit_form_fields(self):
        """Name and done should only be displayed"""
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ["name", "done"])
