from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_items, name="home"),
    path("add/", views.add, name="add"),
    path("edit/<int:primary_key>", views.edit, name="edit"),
    path("toggle/<int:primary_key>", views.toggle, name="toggle"),
    path("delete/<int:primary_key>", views.delete_task, name="delete")
]
