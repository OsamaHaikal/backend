from django.contrib import admin
from .models import Post, Comment ,Tag ,Referece

admin.site.register(Tag)

class RefereceInline(admin.StackedInline):
    model = Referece
class CommentInline(admin.StackedInline):
    model = Comment

class PostAdminSite(admin.AdminSite):
    site_header = "Blog Post admin"
    site_title = "Blog Post Admin Portal"
    index_title = "Editor page"

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [RefereceInline,CommentInline,]
    
post_admin_site = PostAdminSite(name='post_admin')

post_admin_site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)