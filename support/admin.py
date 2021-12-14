from django.contrib import admin
from .models import Faq , Tag , Contact
# Register your models here.
admin.site.register(Faq)
admin.site.register(Tag)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'id')

admin.site.register(Contact, ContactAdmin)
