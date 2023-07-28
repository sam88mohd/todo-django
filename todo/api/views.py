from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from .models import Todo

# Create your views here.


class TodoListView(View):
    def get(self, request):
        context = {}
        todos = Todo.objects.all()
        context['todos'] = todos
        return render(request=request, template_name='api/todolist.html', context=context)


def submit_todo(request):
    title = request.POST['title']
    if title == '':
        messages.error(request, "Input can not be blank!")
    else:
        todo = Todo(title=title)
        todo.save()
    return redirect('todolist')


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todolist')


def update_todo_status(request, todo_id):
    todo = Todo.objects.filter(pk=todo_id)
    todo.update(status=True)
    return redirect('todolist')
