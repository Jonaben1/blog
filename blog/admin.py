from django.contrib import admin
from .models import Post, Category, Comment, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on',)
    list_filter = ('status',)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

admin.site.register(Contact, ContactAdmin)
