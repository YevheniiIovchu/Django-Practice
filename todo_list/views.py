from django.shortcuts import render
from django.views import View, generic

from todo_list.models import Task, Tag


class IndexView(View):
    template_name = "todo_list/index.html"

    def get(self, request):
        return render(request, self.template_name)


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag
