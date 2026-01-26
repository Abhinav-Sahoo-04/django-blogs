from django.shortcuts import render,get_object_or_404,redirect

from blogs.models import Blog, Category
from django.db.models import Q

# Create your views here.

def get_by_category(request,category_id):
    category=get_object_or_404(Category,id=category_id)
    blog=Blog.objects.filter(status="Published",category_id=category_id)
    context={
        "category":category,
        "blog":blog,
    }
    return render(request,"get_by_category.html",context)

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug)
    featured_blog=Blog.objects.filter(is_featured=True).order_by("updated_at")
    context={
        "single_blog":single_blog,
        "featured_blog":featured_blog,
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword=request.GET.get('keyword')
    if len(keyword)==0:
        return redirect('home')
    else:
        blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published" )
        context={
            "blogs":blogs,
        }
        return render(request,'search.html',context)