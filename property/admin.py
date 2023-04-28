from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class AdminFlat(admin.ModelAdmin):
    # list_display = ('town', 'address', 'owner', 'price')
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
