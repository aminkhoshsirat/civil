from django.shortcuts import render, redirect
from .models import Project, Coworking, Category, LateralSys, GravitySys
from django.shortcuts import get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    project = Project.objects.all()
    coworking = Coworking.objects.all()
    return render(request,"index.html", {'Project':project, 'Coworking':coworking})

# def detail(request, id:int, title:str):
#     project = get_object_or_404(Project,id=id)
#     context = {'Projects' : project}
#     return render(request,"detail.html", context)

def detail(request, id, title):
    project = get_object_or_404(Project.objects.prefetch_related('images'), id=id, title=title)
    return render(request, 'detail.html', {'Projects': project})

# def store(request):
#     categories = request.GET.getlist('category')
#     print(categories)  # Debugging line
#     if categories:
#         project = Project.objects.filter(category__title__in=categories)
#     else:
#         project = Project.objects.all()
#     return render(request, "store.html", {'Project': project, 'categories': categories})



# def store(request):
#     # Fetch categories from the database
#     categories = Category.objects.all()
#
#     # Retrieve Gravity, Lateral Systems from the database
#     gravity_systems = GravitySys.objects.all()
#     lateral_systems = LateralSys.objects.all()
#
#     # Get selected categories, floor system, and other filters
#     selected_categories = request.GET.getlist('category')
#     selected_floor_system = request.GET.get('floor_system')
#     selected_lateral_system = request.GET.get('lateral_system')
#     min_area = request.GET.get('min_area')
#     max_area = request.GET.get('max_area')
#
#     # Base query for projects
#     project_query = Project.objects.all()
#
#     # Filter by selected categories
#     if selected_categories:
#         project_query = project_query.filter(category__title__in=selected_categories)
#
#     # Filter by total area
#     if min_area:
#         project_query = project_query.filter(total_Area__gte=min_area)
#     if max_area:
#         project_query = project_query.filter(total_Area__lte=max_area)
#
#     # Filter by floor system
#     if selected_floor_system:
#         project_query = project_query.filter(gravity_loading_sys__title=selected_floor_system)
#
#     # Filter by lateral system
#     if selected_lateral_system:
#         project_query = project_query.filter(lateral_loading_sys__title=selected_lateral_system)
#
#     # Paginate results (6 items per page)
#     paginator = Paginator(project_query, 6)
#     page = request.GET.get('page')
#
#     try:
#         projects = paginator.page(page)
#     except PageNotAnInteger:
#         projects = paginator.page(1)
#     except EmptyPage:
#         projects = paginator.page(paginator.num_pages)
#
#     context = {
#         'Project': projects,
#
#         'categories': categories,  # Pass categories to the template
#         'selected_categories': selected_categories,  # Retain selected categories
#
#         'gravity_systems': gravity_systems,  # Pass GravitySys data to template
#         'selected_floor_system': selected_floor_system,  # Retain selected floor system
#
#         'lateral_systems': lateral_systems,  # Pass GravitySys data to template
#         'selected_lateral_system': selected_lateral_system,  # Retain selected lateral system
#     }
#     return render(request, "store.html", context)

def store(request):
    # Fetch categories from the database
    categories = Category.objects.all()

    # Retrieve Gravity, Lateral Systems from the database
    gravity_systems = GravitySys.objects.all()
    lateral_systems = LateralSys.objects.all()

    # Get selected categories, floor system, and other filters
    selected_categories = request.GET.getlist('category')
    selected_floor_system = request.GET.get('floor_system')
    selected_lateral_system = request.GET.get('lateral_system')
    min_area = request.GET.get('min_area')
    max_area = request.GET.get('max_area')

    # Base query for projects
    project_query = Project.objects.all()

    # Filter by selected categories
    if selected_categories:
        project_query = project_query.filter(category__title__in=selected_categories)

    # Filter by total area
    if min_area:
        project_query = project_query.filter(total_Area__gte=min_area)
    if max_area:
        project_query = project_query.filter(total_Area__lte=max_area)

    # Filter by floor system
    if selected_floor_system:
        project_query = project_query.filter(gravity_loading_sys__title=selected_floor_system)

    # Filter by lateral system
    if selected_lateral_system:
        project_query = project_query.filter(lateral_loading_sys__title=selected_lateral_system)

    # Paginate results (6 items per page)
    paginator = Paginator(project_query, 6)
    page = request.GET.get('page')

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    # Build query string for pagination links
    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page')

    context = {
        'Project': projects,
        'page_obj': projects,
        'categories': categories,
        'selected_categories': selected_categories,
        'gravity_systems': gravity_systems,
        'selected_floor_system': selected_floor_system,
        'lateral_systems': lateral_systems,
        'selected_lateral_system': selected_lateral_system,
        'query_string': query_params.urlencode(),  # Pass the query string to the template
    }
    return render(request, "store.html", context)

