from django.shortcuts import render
from .models import About, Skill





def about(request):
    about = About.objects.all().last()
    skills = Skill.objects.all()
    context = {
        'about':about,
        'skills':skills,
    }

    return render(request, 'about/about.html', context)

