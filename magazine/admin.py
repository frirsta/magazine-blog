from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Profile


class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'author', 'post_created']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    ordering = ['post_created']


admin.site.register(Post, AdminPost)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)

# Register your models here.
