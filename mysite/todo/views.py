from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "todo/todo.html", context)


def add(request):
    form = ItemForm
    context = {"form": form}
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "todo/add.html", context)


def edit(request, primary_key):
    task = get_object_or_404(Item, pk=primary_key)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = ItemForm(instance=task)
    context = {
        "task": form
    }
    return render(request, "todo/edit.html", context)


def toggle(request, primary_key):
    task = get_object_or_404(Item, pk=primary_key)
    task.done = not task.done
    task.save()
    return redirect("home")


def delete_task(request, primary_key):
    task = get_object_or_404(Item, pk=primary_key)
    task.delete()
    return redirect("home")
