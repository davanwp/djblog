from django.contrib import admin
from blog.models import Post, Category, Comment, Contact

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_categories', 'created_on', 'last_modified']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title', )}

    def get_categories(self, obj):
        return "\n".join([c.name for c in obj.categories.all()])
    
    get_categories.short_description = 'Categories'

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['name']
   search_fields = ['name']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author']
    search_fields = ['author']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','address','message','show_image','created_on','updated_on']
    search_fields = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)