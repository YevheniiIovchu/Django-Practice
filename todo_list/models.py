from django.db import models


class Tag (models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=63)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
