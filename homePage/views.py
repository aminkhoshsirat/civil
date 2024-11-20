from django.shortcuts import render, redirect
from .models import Project, Coworking, Category
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

# def store(request):
#     categories = request.GET.getlist('category')
#     print(categories)  # Debugging line
#     if categories:
#         project = Project.objects.filter(category__title__in=categories)
#     else:
#         project = Project.objects.all()
#     return render(request, "store.html", {'Project': project, 'categories': categories})




def store(request):
    categories = request.GET.getlist('category')  # Selected categories
    min_area = request.GET.get('min_area')
    max_area = request.GET.get('max_area')
    floor_system = request.GET.get('floor_system')

    # Base Query
    project_query = Project.objects.all()

    # Filter by categories
    if categories:
        project_query = project_query.filter(category__title__in=categories)

    # Filter by total area
    if min_area:
        project_query = project_query.filter(total_Area__gte=min_area)
    if max_area:
        project_query = project_query.filter(total_Area__lte=max_area)



    categories = [
        {'original': 'Steel Structures', 'translated': 'سازه های فولادی'},
        {'original': 'Concrete Structures', 'translated': 'سازه های بتن آرمه'},
        {'original': 'Industrial Structures', 'translated': 'سازه های صنعتی'},
    ]

    # Category translations
    category_translations = {
        "Steel Structures": "سازه های فولادی",
        "Concrete Structures": "سازه های بتن آرمه",
        "Industrial Structures": "سازه های صنعتی",
    }


    # Retrieve distinct categories from the Project model
    distinct_categories = Project.objects.values_list('category__title', flat=True).distinct()

    # Translate categories
    translated_categories = [
        {
            "original": category,
            "translated": category_translations.get(category, category)
        }
        for category in distinct_categories
    ]

    # Pass data to the template
    context = {
        'Project': project_query,
        'categories': translated_categories,  # Pass translated categories
        'selected_categories': categories,    # Retain selected categories for checkbox state
    }
    return render(request, "store.html", context)