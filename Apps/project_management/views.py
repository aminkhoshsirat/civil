from .models import ProjManProject, ProjManCoworking, ProjManCategory
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Q

from django.views.generic import TemplateView, DetailView
from .models import ProjManProject, ProjManCoworking
from django.views.generic.list import ListView

# def index(request):
#     project = ProjManProject.objects.prefetch_related('images')  # Adjust 'images' to the related_name for Project images
#     coworking = ProjManCoworking.objects.prefetch_related('images', 'category')  # Prefetch images and category for Coworking
#     return render(request, "index2.html", {'Project': project, 'Coworking': coworking})

class IndexView(TemplateView):
    template_name = "project_management/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch projects (adjust if 'images' is related_name in STRProject)
        context['ProjManProject'] = ProjManProject.objects.all()

        # Fetch coworking projects and include category
        context['Coworking'] = ProjManCoworking.objects.select_related('category')
        print(context['Coworking'])  # Debug: Ensure objects are fetched correctly
        return context



class ProjectDetailView(DetailView):
    model = ProjManProject
    template_name = 'project_management/detail.html'
    context_object_name = 'Project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = ProjManProject.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context



class CoworkingDetailView(DetailView):
    model = ProjManCoworking
    template_name = 'project_management/coworkings_detail.html'
    context_object_name = 'Coworking'
    slug_field = 'slug'
    slug_url_kwarg = 'title'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_coworkings'] = ProjManCoworking.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context


class StoreView(ListView):
    model = ProjManProject
    template_name = 'project_management/store.html'
    context_object_name = 'Project'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        selected_categories = self.request.GET.getlist('category')
        min_area = self.request.GET.get('min_area')
        max_area = self.request.GET.get('max_area')

        if selected_categories:
            query = query.filter(category__title__in=selected_categories)
        if min_area:
            query = query.filter(total_Area__gte=min_area)
        if max_area:
            query = query.filter(total_Area__lte=max_area)

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjManCategory.objects.all()
        context['query_string'] = self.request.GET.urlencode()
        return context


class SearchView(ListView):
    model = ProjManProject
    template_name = 'project_management/search.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return ProjManProject.objects.filter(
            Q(title__icontains=query) |
            Q(category__title__icontains=query) |
            Q(content__icontains=query)
        ).distinct() if query else ProjManProject.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class ProjectsView(ListView):
    model = ProjManProject
    template_name = 'project_management/projects.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return ProjManProject.objects.filter(content__icontains='پروژه شاخص')



class CoworkingsView(ListView):
    model = ProjManCoworking
    template_name = 'project_management/coworkings.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):

        for coworking in ProjManCoworking.objects.all():
            print(coworking.image.url)


        return ProjManCoworking.objects.filter(content__icontains='پروژه شاخص')



class MentoringView(TemplateView):
    template_name = 'project_management/mentoring.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Project'] = ProjManProject.objects.prefetch_related('images')
        context['Coworking'] = ProjManCoworking.objects.prefetch_related('images', 'category')
        return context

class ContactUsView(TemplateView):
    template_name = 'project_management/contact_us.html'







# def detail(request, id:int, title:str):
#     project = get_object_or_404(ProjManProject.objects.prefetch_related('images'),id=id)
#     related_projects = ProjManProject.objects.filter(category=project.category).exclude(id=project.id)[:4]
#
#     context = {'Project' : project, 'related_projects': related_projects}
#     return render(request,"detail.html", context)
#
# def coworking_detail(request, id: int, title: str):
#     coworking = get_object_or_404(ProjManCoworking.objects.prefetch_related('images'), id=id, slug=title)
#     related_coworkings = ProjManCoworking.objects.filter(category=coworking.category).exclude(id=coworking.id)[:4]
#
#     context = {'Coworking' : coworking, 'related_coworkings': related_coworkings}
#     return render(request,"coworkings_detail.html", context)
#
# def store(request):
#     # Fetch categories from the database
#     categories = ProjManCategory.objects.all()
#
#     # Get selected categories, floor system, and other filters
#     selected_categories = request.GET.getlist('category')
#     selected_floor_system = request.GET.get('floor_system')
#     selected_lateral_system = request.GET.get('lateral_system')
#     min_area = request.GET.get('min_area')
#     max_area = request.GET.get('max_area')
#
#     # Base query for projects
#     project_query = ProjManProject.objects.all()
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
#         'query_string': query_params.urlencode(),  # Pass the query string to the template
#     }
#     return render(request, "store.html", context)
#
# def search(request):
#     query = request.GET.get('q', '')
#     projects = ProjManProject.objects.filter(
#         Q(title__icontains=query) |
#         Q(category__title__icontains=query) |
#         Q(content__icontains=query)
#     ).distinct() if query else ProjManProject.objects.none()
#
#     # Paginate results
#     paginator = Paginator(projects, 9)  # 9 projects per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'search.html', {'projects': page_obj, 'query': query})
#
# def projects(request):
#     project = ProjManProject.objects.prefetch_related('images')
#     # Filter projects containing 'پروژه شاخص' in the content field
#     featured_projects = ProjManProject.objects.filter(content__icontains='پروژه شاخص')
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
#     coworking = ProjManCoworking.objects.prefetch_related('images', 'category')
#     # Filter projects containing 'پروژه شاخص' in the content field
#     featured_coworking = ProjManCoworking.objects.filter(content__icontains='پروژه شاخص')
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
#     project = ProjManProject.objects.prefetch_related('images')
#     coworking = ProjManCoworking.objects.prefetch_related('images', 'category')
#     return render(request, "mentoring.html", {'Project': project, 'Coworking': coworking})
#
# def contact_us(request):
#     return render(request, "contact_us.html")