from django.shortcuts import render
from .models import Tarea

# Create your views here.

def saludar(request):
    context = {}
    if request.method == 'GET':
        tareas = Tarea.objects.all()
        context['tareas'] = tareas
    return render(request, "todoList/main.html",context)

