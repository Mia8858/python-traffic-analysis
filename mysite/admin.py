from django.contrib import admin
from mysite.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'body')

admin.site.register(Post, PostAdmin)