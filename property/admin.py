from django.contrib import admin

from .models import Flat, Complaint


@admin.register(Flat)
class AdminFlat(admin.ModelAdmin):

    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('active', 'new_building', 'rooms_number', 'has_balcony', 'floor',)
    search_fields = ['town', 'address', 'construction_year', 'owner_pure_phone']
    raw_id_fields = ('liked_by',)
    readonly_fields = ['created_at',]


@admin.register(Complaint)
class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ('user', 'address')
    search_fields = ('user__username',)



