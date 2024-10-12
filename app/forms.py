from django import forms
from app.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
