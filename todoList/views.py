# Create your views here.

from django.shortcuts import render
from .models import Tarea
from .forms import TareaForm

def saludar(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        print("------- FORMULARIO CON DATOS ----------")
        print(form)
        if form.is_valid():
            form.save()
    form = TareaForm()
    #print(form)
    tareas = Tarea.objects.all() #-> Lista de objetos
    context = {'tareas':tareas,'form':form}
    return render(request,'base.html',context)

