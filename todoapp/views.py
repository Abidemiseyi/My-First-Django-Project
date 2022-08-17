from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import TodoListItem


# Create your views here.


def home(request):
    todo_item = TodoListItem.objects.all().order_by('-added_date')
    return render(request, 'todolist.html', {
        'todo_items': todo_item
    })


@ csrf_exempt
def add_todo(request):
    print(request.POST)
    current_date = timezone.now()
    content = request.POST['content']
    created_obj = TodoListItem.objects.create(
        added_date=current_date, text=content)
    length_of_todo = TodoListItem.objects.all().count()
    return HttpResponseRedirect("/todoapp")


@ csrf_exempt
def delete_todo(request, todo_id):
    TodoListItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/todoapp")
