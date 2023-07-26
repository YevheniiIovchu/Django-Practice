from django.contrib import admin

from todo_list.models import Task, Tag


@admin.register(Task)
class DishAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("tag",)


@admin.register(Tag)
class DishTypeAdmin(admin.ModelAdmin):
    pass
