from django.shortcuts import render, redirect
from .models import Project, Coworking
from django.shortcuts import get_object_or_404, redirect, reverse


# Create your views here.
def index(request):
    project = Project.objects.all()
    coworking = Coworking.objects.all()
    return render(request,"index.html", {'Project':project, 'Coworking':coworking})

def detail(request, id:int, title:str):
    project = get_object_or_404(Project,id=id)
    context = {'Projects' : project}
    return render(request,"detail.html", context)

def store(request):
    category = request.GET.get('category')
    if category is not None:
        project = Project.objects.filter(category__title=category)
    else:
        project = Project.objects.all()
    return render(request,"store.html", {'Projects':project})
