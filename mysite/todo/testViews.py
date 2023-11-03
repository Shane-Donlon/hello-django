from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/todo.html")

    def test_get_add_item_page(self):
        response = self.client.get("/add/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/add.html")

    def test_get_edit_item_page(self):
        taskDone = Item.objects.create(name="testing todo", done=True)
        taskNotDOne = Item.objects.create(name="testing todo", done=False)
        response = self.client.get(f"/edit/{taskDone.id}")
        responseNotDone = self.client.get(f"/edit/{taskNotDOne.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseNotDone.status_code, 200)
        self.assertTemplateUsed("todo/edit.html")

    def test_get_add_item(self):
        response = self.client.post("/add", {"name": "Testing add item"})
        self.assertEqual(response.status_code, 301)

    def test_get_delete_item(self):
        task = Item.objects.create(name="Testing Item Deletion")
        response = self.client.get(f"/delete/{task.id}")
        self.assertRedirects(response, "/")
        existing_item = Item.objects.filter(id=task.id)
        self.assertEqual(len(existing_item), 0)

    def test_get_toggle_item(self):
        task = Item.objects.create(name="testing done toggle", done=True)
        response = self.client.get(f"/toggle/{task.id}")

        self.assertRedirects(response, "/")
        updated_item = Item.objects.get(id=task.id)
        self.assertEqual(updated_item.done, False)

    def test_can_edit_task(self):
        task = Item.objects.create(name="testing done toggle", done=True)
        task = Item.objects.get(id=task.id)
        response = self.client.post(
            f"/edit/{task.id}", {"name": "updated"})
        self.assertRedirects(response, "/")
        updated_item = Item.objects.get(id=task.id)
        self.assertEqual(updated_item.name, "updated")
