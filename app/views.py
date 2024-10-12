from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, Tag
from .forms import TaskForm, TagForm


class HomeView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'
    ordering = ['completed', '-created_at']


class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('home')


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_object_or_404(Task, pk=self.kwargs['pk'])


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete_task.html'  # Optional: you can create a template for confirmation
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_object_or_404(Task, pk=self.kwargs['pk'])


class CompleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
        return redirect('home')


class AddTagView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'add_tag.html'
    success_url = reverse_lazy('tag_list')


class UpdateTagView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'update_tag.html'
    success_url = reverse_lazy('tag_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Tag, pk=self.kwargs['pk'])


class DeleteTagView(DeleteView):
    model = Tag
    template_name = 'delete_tag.html'  # Optional: you can create a template for confirmation
    success_url = reverse_lazy('tag_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Tag, pk=self.kwargs['pk'])
