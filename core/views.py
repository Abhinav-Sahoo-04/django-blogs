from django.shortcuts import render

#THIS IS HOME PAGE
def home(request):
    return render(request,'home.html')
