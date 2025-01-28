from django.urls import path
from . import views
from .views import IndexView

app_name = 'BIM'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
]
