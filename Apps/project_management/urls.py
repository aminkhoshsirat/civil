from django.urls import path
from . import views
from .views import IndexView

app_name = 'project_management'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('store/', views.store, name='store'),
    # path('<int:id>/<str:title>/', views.detail, name='detail'),
    # path('coworkings_detail/<int:id>/<slug:title>/', views.coworking_detail, name='coworking_detail'),
    # path('search/', views.search, name='search'),
    # path('projects/', views.projects, name='projects'),
    # path('coworkings/', views.coworkings, name='coworkings'),
    # path('mentoring/', views.mentoring, name='mentoring'),
    # path('contact_us/', views.contact_us, name='contact_us'),

    path('', IndexView.as_view(), name='index'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('coworkings_detail/<int:id>/<slug:title>/', views.CoworkingDetailView.as_view(), name='coworking_detail'),
    path('store/', views.StoreView.as_view(), name='store'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('coworkings/', views.CoworkingsView.as_view(), name='coworkings'),
    path('mentoring/', views.MentoringView.as_view(), name='mentoring'),
    path('contact_us/', views.ContactUsView.as_view(), name='contact_us'),

]
