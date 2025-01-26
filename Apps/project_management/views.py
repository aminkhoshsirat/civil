from .models import ProjManProject, ProjManCoworking, ProjManCategory
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Q


def index(request):
    project = ProjManProject.objects.prefetch_related('images')  # Adjust 'images' to the related_name for Project images
    coworking = ProjManCoworking.objects.prefetch_related('images', 'category')  # Prefetch images and category for Coworking
    return render(request, "index.html", {'Project': project, 'Coworking': coworking})

def detail(request, id:int, title:str):
    project = get_object_or_404(ProjManProject.objects.prefetch_related('images'),id=id)
    related_projects = ProjManProject.objects.filter(category=project.category).exclude(id=project.id)[:4]

    context = {'Project' : project, 'related_projects': related_projects}
    return render(request,"detail.html", context)

def coworking_detail(request, id: int, title: str):
    coworking = get_object_or_404(ProjManCoworking.objects.prefetch_related('images'), id=id, slug=title)
    related_coworkings = ProjManCoworking.objects.filter(category=coworking.category).exclude(id=coworking.id)[:4]

    context = {'Coworking' : coworking, 'related_coworkings': related_coworkings}
    return render(request,"coworkings_detail.html", context)

def store(request):
    # Fetch categories from the database
    categories = ProjManCategory.objects.all()

    # Get selected categories, floor system, and other filters
    selected_categories = request.GET.getlist('category')
    selected_floor_system = request.GET.get('floor_system')
    selected_lateral_system = request.GET.get('lateral_system')
    min_area = request.GET.get('min_area')
    max_area = request.GET.get('max_area')

    # Base query for projects
    project_query = ProjManProject.objects.all()

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
        'query_string': query_params.urlencode(),  # Pass the query string to the template
    }
    return render(request, "store.html", context)

def search(request):
    query = request.GET.get('q', '')
    projects = ProjManProject.objects.filter(
        Q(title__icontains=query) |
        Q(category__title__icontains=query) |
        Q(content__icontains=query)
    ).distinct() if query else ProjManProject.objects.none()

    # Paginate results
    paginator = Paginator(projects, 9)  # 9 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search.html', {'projects': page_obj, 'query': query})

def projects(request):
    project = ProjManProject.objects.prefetch_related('images')
    # Filter projects containing 'پروژه شاخص' in the content field
    featured_projects = ProjManProject.objects.filter(content__icontains='پروژه شاخص')

    # Paginate the filtered projects
    paginator = Paginator(featured_projects, 3)  # Show 3 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass only 'page_obj' to the template for paginated results
    context = {'Project': project ,'page_obj': page_obj}
    return render(request, 'projects.html', context)

def coworkings(request):
    coworking = ProjManCoworking.objects.prefetch_related('images', 'category')
    # Filter projects containing 'پروژه شاخص' in the content field
    featured_coworking = ProjManCoworking.objects.filter(content__icontains='پروژه شاخص')

    # Paginate the filtered projects
    paginator = Paginator(featured_coworking, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass only 'page_obj' to the template for paginated results
    context = {'Coworking': coworking ,'page_obj': page_obj}
    return render(request, 'coworkings.html', context)

def mentoring(request):
    project = ProjManProject.objects.prefetch_related('images')
    coworking = ProjManCoworking.objects.prefetch_related('images', 'category')
    return render(request, "mentoring.html", {'Project': project, 'Coworking': coworking})

def contact_us(request):
    return render(request, "contact_us.html")