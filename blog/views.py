from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.


def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}

    return render(request, 'blogs/blogs.html', context)
    

def blog(request, b_id):
    blog = get_object_or_404(Blog, pk = b_id)
    context = {'blog':blog}
    return render(request, 'blogs/blog.html', context)