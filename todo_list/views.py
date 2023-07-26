from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "todo_list/task_create.html"
    success_url = reverse_lazy("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag
