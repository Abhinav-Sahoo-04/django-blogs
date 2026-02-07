from django.contrib import admin
from .models import Category,Blog,Comment
#user abhinav pass abhinav13
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':('title',)
    }
    # list_display=('id','title','category','status','is_featured')
    search_fields=('id','title','category__category_name','status',)
    # list_editable=('is_featured','status','category')

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)