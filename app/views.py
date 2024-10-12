from django.urls import reverse_lazy
from django.views import generic
from app.models import Todo
from app.forms import TodoForm


class TodoListView(generic.ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'


class TodoCreateView(generic.CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'add_todo.html'
    success_url = reverse_lazy('todo_list')


class TodoUpdateView(generic.UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'update_todo.html'
    success_url = reverse_lazy('todo_list')

    def get_object(self, queryset=None):
        # Override to provide the object to update
        return Todo.objects.get(pk=self.kwargs['pk'])
