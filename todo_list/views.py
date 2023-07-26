from django.shortcuts import render
from django.views import View, generic

from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/index.html"


class TagListView(generic.ListView):
    model = Tag
