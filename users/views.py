from django.shortcuts import render
from projects.models import Project
from clients.models import Client
from about.models import About
from blog.models import Blog



def dashboard(request):
    projects = Project.objects.all()
    clinets = Client.objects.all()
    abouts = About.objects.all().last()
    blogs = Blog.objects.all()
    context = {
        'projects':projects,
        'clients':clinets,
        'abouts':abouts,
        'blogs':blogs,
        }
    
    return render(request, 'users/dashboard.html', context)
