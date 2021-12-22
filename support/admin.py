from django.contrib import admin
from .models import Faq , Tag , Contact
from blog.admin import post_admin_site
# Register your models here.
admin.site.register(Tag)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'id')

admin.site.register(Contact, ContactAdmin)


post_admin_site.register(Faq)

