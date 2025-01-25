from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Apps.Home_Page.urls', namespace='Home_Page')),

    path('structure_design/', include('Apps.Structure_Design.urls', namespace='Structure_Design')),
    path('bim/', include('Apps.BIM.urls', namespace='BIM')),
    path('project_management/', include('Apps.project_management.urls', namespace='project_management')),
    path('retrofit/', include('Apps.Retrofit.urls', namespace='Retrofit')),
    path('software/', include('Apps.Software.urls', namespace='Software')),
    path('users/', include('Apps.Users.urls', namespace='Users')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)