from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'), 
    path('resume/', views.resume, name='resume'),
    path('resume/pdf/', views.resume_pdf, name='resume_pdf'),
    path('testimonials/', views.testimonials, name='testimonials'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
