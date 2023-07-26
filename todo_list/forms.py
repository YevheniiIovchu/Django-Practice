from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from todo_list.models import Tag, Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"

    def clean_deadline(self):
        cleaned_data = super().clean()
        deadline = cleaned_data.get("deadline", timezone.now())

        if deadline < timezone.now():
            raise ValidationError("Deadline cannot be before the creation of the task.")
        if deadline <= timezone.now() + timedelta(minutes=30):
            raise ValidationError("Deadline must be at least 30 minutes from the creation of the task.")

        return cleaned_data
