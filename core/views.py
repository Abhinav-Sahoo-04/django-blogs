from django.shortcuts import render
from blogs.models import Category,Blog
#THIS IS HOME PAGE
def home(request):
    featured_blog=Blog.objects.filter(is_featured=True).order_by("updated_at")
    blog=Blog.objects.filter(is_featured=False,status='Published')
    context ={
        "featured_blog":featured_blog,
        "blog":blog,

    }
    return render(request,'home.html',context)

