from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Profile, Comment


class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'author', 'post_created']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    ordering = ['post_created']


admin.site.register(Post, AdminPost)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'post', 'comment_created')
    list_filter = ('comment_created',)
    search_fields = ('user', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
