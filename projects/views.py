from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project

def project_list(request):
    qs = Project.objects.all()
    paginator = Paginator(qs, 6)  # 6 projects per page (tweak as desired)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'projects/project_list.html', {'page_obj': page_obj, 'projects': page_obj.object_list})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})
