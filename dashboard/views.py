from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count()
    posts_count=Blog.objects.all().count()
    context={
        "category_count":category_count,
        "posts_count":posts_count,
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        form.save()
        return redirect('add_category')
    form=CategoryForm()
    context={
        "form":form,
    }
    return render(request,'dashboard/add_categories.html',context)

def edit_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    form=CategoryForm(instance=category)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    context={
        "form":form,
        "category":category,
    }
    return render(request,'dashboard/edit_categories.html',context)

def delete_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')