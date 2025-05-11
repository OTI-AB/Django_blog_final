from django.contrib import admin
from blogs.models import Category, Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields =  {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured', 'created_at', 'updated_at' )
    search_fields = ('id', 'title', 'category__cat_name', 'status')
    list_editable = ['is_featured']


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
