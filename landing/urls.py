from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('<int:id>/<str:title>/', views.detail, name='detail'),
    path('coworkings_detail/<int:id>/<slug:title>/', views.coworking_detail, name='coworking_detail'),
]
