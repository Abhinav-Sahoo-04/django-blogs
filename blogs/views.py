from django.shortcuts import render,get_object_or_404

from blogs.models import Blog, Category

# Create your views here.

def get_by_category(request,category_id):
    category=get_object_or_404(Category,id=category_id)
    blog=Blog.objects.filter(status="Published",category_id=category_id)
    context={
        "category":category,
        "blog":blog,
    }
    return render(request,"get_by_category.html",context)