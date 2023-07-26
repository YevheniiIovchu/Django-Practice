from django.urls import path

from todo_list.views import TagListView, TaskListView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo_list"
