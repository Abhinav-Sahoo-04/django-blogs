from django.contrib import admin
from .models import Catagory,Blog
#user abhinav pass abhinav13
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':('title',)
    }
    list_display=('id','title','catagory','status','is_featured')
    search_fields=('id','title','catagory__catagory_name','status',)
    list_editable=('is_featured',)

admin.site.register(Catagory)
admin.site.register(Blog,BlogAdmin)