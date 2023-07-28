from django.urls import path, include
from . import views

urlpatterns = [
    path(route='', view=views.TodoListView.as_view(), name='todolist'),
    path(route='submit/', view=views.submit_todo, name='submit'),
    path(route='deleteitem/<int:todo_id>',
         view=views.delete_todo, name='deleteitem'),
    path(route='updatestatus/<int:todo_id>', view=views.update_todo_status, name='updatestatus')
]
