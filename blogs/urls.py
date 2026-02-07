from django.urls import path
from . import views
urlpatterns=[
    path('<int:category_id>/',views.get_by_category,name='get_by_category'),
    path('most_popular/',views.most_popular,name='most_popular')
]