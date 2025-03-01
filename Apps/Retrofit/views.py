from .models import RetroProject, RetroCoworking, RetroCategory, RetroLateralSys, RetroGravitySys
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Q

from django.views.generic import TemplateView, DetailView
from .models import RetroProject, RetroCoworking
from django.views.generic.list import ListView

# def index(request):
#     project = RetroProject.objects.prefetch_related('images')  # Adjust 'images' to the related_name for Project images
#     coworking = RetroCoworking.objects.prefetch_related('images', 'category')  # Prefetch images and category for Coworking
#     return render(request, "Retrofit/index2.html", {'Project': project, 'Coworking': coworking})

class IndexView(TemplateView):
    template_name = "Retrofit/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch projects (adjust if 'images' is related_name in STRProject)
        context['RetroProject'] = RetroProject.objects.all()

        # Fetch coworking projects and include category
        context['Coworking'] = RetroCoworking.objects.select_related('category')
        print(context['Coworking'])  # Debug: Ensure objects are fetched correctly
        return context


class ProjectDetailView(DetailView):
    model = RetroProject
    template_name = 'Retrofit/detail.html'
    context_object_name = 'Project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = RetroProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class CoworkingDetailView(DetailView):
    model = RetroCoworking
    template_name = 'Retrofit/coworkings_detail.html'
    context_object_name = 'Coworking'
    slug_field = 'slug'
    slug_url_kwarg = 'title'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_coworkings'] = RetroCoworking.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class StoreView(ListView):
    model = RetroProject
    template_name = 'Retrofit/store.html'
    context_object_name = 'Project'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        selected_categories = self.request.GET.getlist('category')
        selected_floor_system = self.request.GET.get('floor_system')
        selected_lateral_system = self.request.GET.get('lateral_system')
        min_area = self.request.GET.get('min_area')
        max_area = self.request.GET.get('max_area')

        if selected_categories:
            query = query.filter(category__title__in=selected_categories)
        if min_area:
            query = query.filter(total_Area__gte=min_area)
        if max_area:
            query = query.filter(total_Area__lte=max_area)
        if selected_floor_system:
            query = query.filter(gravity_loading_sys__title=selected_floor_system)
        if selected_lateral_system:
            query = query.filter(lateral_loading_sys__title=selected_lateral_system)

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = RetroCategory.objects.all()
        context['gravity_systems'] = RetroGravitySys.objects.all()
        context['lateral_systems'] = RetroLateralSys.objects.all()
        context['query_string'] = self.request.GET.urlencode()
        return context





class SearchView(ListView):
    model = RetroProject
    template_name = 'Retrofit/search.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return RetroProject.objects.filter(
            Q(title__icontains=query) |
            Q(category__title__icontains=query) |
            Q(content__icontains=query)
        ).distinct() if query else RetroProject.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class ProjectsView(ListView):
    model = RetroProject
    template_name = 'Retrofit/projects.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return RetroProject.objects.filter(content__icontains='پروژه شاخص')



class CoworkingsView(ListView):
    model = RetroCoworking
    template_name = 'Retrofit/coworkings.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):

        for coworking in RetroCoworking.objects.all():
            print(coworking.image.url)


        return RetroCoworking.objects.filter(content__icontains='پروژه شاخص')


class MentoringView(TemplateView):
    template_name = 'Retrofit/mentoring.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Project'] = RetroProject.objects.prefetch_related('images')
        context['Coworking'] = RetroCoworking.objects.prefetch_related('images', 'category')
        return context

class ContactUsView(TemplateView):
    template_name = 'Retrofit/contact_us.html'



# def detail(request, id:int, title:str):
#     project = get_object_or_404(RetroProject.objects.prefetch_related('images'),id=id)
#     related_projects = RetroProject.objects.filter(category=project.category).exclude(id=project.id)[:4]
#
#     context = {'Project' : project, 'related_projects': related_projects}
#     return render(request,"detail.html", context)
#
# def coworking_detail(request, id: int, title: str):
#     coworking = get_object_or_404(RetroCoworking.objects.prefetch_related('images'), id=id, slug=title)
#     related_coworkings = RetroCoworking.objects.filter(category=coworking.category).exclude(id=coworking.id)[:4]
#
#     context = {'Coworking' : coworking, 'related_coworkings': related_coworkings}
#     return render(request,"coworkings_detail.html", context)
#
# def store(request):
#     # Fetch categories from the database
#     categories = RetroCategory.objects.all()
#
#     # Retrieve Gravity, Lateral Systems from the database
#     gravity_systems = RetroGravitySys.objects.all()
#     lateral_systems = RetroLateralSys.objects.all()
#
#     # Get selected categories, floor system, and other filters
#     selected_categories = request.GET.getlist('category')
#     selected_floor_system = request.GET.get('floor_system')
#     selected_lateral_system = request.GET.get('lateral_system')
#     min_area = request.GET.get('min_area')
#     max_area = request.GET.get('max_area')
#
#     # Base query for projects
#     project_query = RetroProject.objects.all()
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
#     # Build query string for pagination links
#     query_params = request.GET.copy()
#     if 'page' in query_params:
#         query_params.pop('page')
#
#     context = {
#         'Project': projects,
#         'page_obj': projects,
#         'categories': categories,
#         'selected_categories': selected_categories,
#         'gravity_systems': gravity_systems,
#         'selected_floor_system': selected_floor_system,
#         'lateral_systems': lateral_systems,
#         'selected_lateral_system': selected_lateral_system,
#         'query_string': query_params.urlencode(),  # Pass the query string to the template
#     }
#     return render(request, "store.html", context)
#
# def search(request):
#     query = request.GET.get('q', '')
#     projects = RetroProject.objects.filter(
#         Q(title__icontains=query) |
#         Q(category__title__icontains=query) |
#         Q(content__icontains=query)
#     ).distinct() if query else RetroProject.objects.none()
#
#     # Paginate results
#     paginator = Paginator(projects, 9)  # 9 projects per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'search.html', {'projects': page_obj, 'query': query})
#
# def projects(request):
#     project = RetroProject.objects.prefetch_related('images')
#     # Filter projects containing 'پروژه شاخص' in the content field
#     featured_projects = RetroProject.objects.filter(content__icontains='پروژه شاخص')
#
#     # Paginate the filtered projects
#     paginator = Paginator(featured_projects, 3)  # Show 3 projects per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     # Pass only 'page_obj' to the template for paginated results
#     context = {'Project': project ,'page_obj': page_obj}
#     return render(request, 'projects.html', context)
#
# def coworkings(request):
#     coworking = RetroCoworking.objects.prefetch_related('images', 'category')
#     # Filter projects containing 'پروژه شاخص' in the content field
#     featured_coworking = RetroCoworking.objects.filter(content__icontains='پروژه شاخص')
#
#     # Paginate the filtered projects
#     paginator = Paginator(featured_coworking, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     # Pass only 'page_obj' to the template for paginated results
#     context = {'Coworking': coworking ,'page_obj': page_obj}
#     return render(request, 'coworkings.html', context)
#
# def mentoring(request):
#     project = RetroProject.objects.prefetch_related('images')
#     coworking = RetroCoworking.objects.prefetch_related('images', 'category')
#     return render(request, "mentoring.html", {'Project': project, 'Coworking': coworking})
#
# def contact_us(request):
#     return render(request, "contact_us.html")