from django.urls import path
from . import views



urlpatterns = [
    path('blogs/', views.blogs, name = 'blogs'),
    path('blog/<int:b_id>', views.blog, name = 'blog'),
    
]