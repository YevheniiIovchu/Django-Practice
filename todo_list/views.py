from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from todo_list.forms import TaskForm
from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_list/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo_list/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list:tag-list")


class CompleteTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = True
        task.save()
        return redirect('todo_list:index')


class UndoTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = False
        task.save()
        return redirect('todo_list:index')
