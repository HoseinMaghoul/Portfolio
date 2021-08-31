from django.shortcuts import render, get_object_or_404
from .models import Project





def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)


def project(request, p_id):
    project = get_object_or_404(Project, pk = p_id )
    context = {'project':project}
    return render(request, 'projects/project.html', context)    