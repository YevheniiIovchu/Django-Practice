from django.urls import path

from todo_list.views import (
    TagListView,
    TaskListView,
    TaskCreateView,
    TagCreateView,
    TaskUpdateView,
    TagUpdateView,
    TaskDeleteView,
    TagDeleteView, CompleteTaskView, UndoTaskView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("<int:pk>/complete/", CompleteTaskView.as_view(), name="task-complete"),
    path("<int:pk>/undo/", UndoTaskView.as_view(), name="task-undo"),
]

app_name = "todo_list"
