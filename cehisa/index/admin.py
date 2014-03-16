from django.contrib import admin
from index.models import Menu

class MenuAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['text']}),
    ]
    list_display = ('text')
    search_fields = ['text']

admin.site.register(Menu)

