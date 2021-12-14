from django.contrib import admin
from .models import Profile, Skill , Project

class RefereceInline(admin.StackedInline):
    model = Project
class SkillInline(admin.StackedInline):
    model = Skill


class Profileadmin(admin.ModelAdmin):
    list_display = ('name','roles','profile_image','created')
    list_filter = ("roles",)
    search_fields = ['title', 'short_intro']
    inlines = [RefereceInline,SkillInline,]

admin.site.register(Profile, Profileadmin)

# Register your models here.
