from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    def test_done_false_default(self):
        task = Item.objects.create(name="Testing False on default")
        self.assertEqual(task.done, False)

    def test_string_returns_name(self):
        task = Item.objects.create(name="Testing todo")
        self.assertEqual(task.__str__(),
                         f"{task.id} {task.name} {task.done}")
