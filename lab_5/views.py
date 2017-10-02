from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Todo_Form
from .models import Todo
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse


# Create your views here.
response = {}
def index(request):    
    response['author'] = "Kezia Irene Tesiman" #TODO Implement yourname
    todo = Todo.objects.all()
    response['todo'] = todo
    html = 'lab_5/lab_5.html'
    response['todo_form'] = Todo_Form
    return render(request, html, response)

def add_todo(request):
    form = Todo_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['title'] = request.POST['title']
        response['description'] = request.POST['description']
        todo = Todo(title=response['title'],description=response['description'])
        todo.save()
        return HttpResponseRedirect('/lab-5/')
    else:
        return HttpResponseRedirect('/lab-5/')

def delete(request, id):
    get_object_or_404(Todo, pk=id).delete()
    return HttpResponseRedirect('/lab-5/')