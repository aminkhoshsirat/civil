from django.urls import path
from . import views

app_name = 'Retrofit'

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('<int:id>/<str:title>/', views.detail, name='detail'),
    path('coworkings_detail/<int:id>/<slug:title>/', views.coworking_detail, name='coworking_detail'),
    path('search/', views.search, name='search'),
    path('projects/', views.projects, name='projects'),
    path('coworkings/', views.coworkings, name='coworkings'),
    path('mentoring/', views.mentoring, name='mentoring'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
