from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from portfolio_site import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('blog/', include('blog.urls', namespace='blog')),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)