from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersInline(admin.TabularInline):
    model = Owner.apartments.through
    extra = 1
    raw_id_fields = ('owner', 'flat')


@admin.register(Flat)
class AdminFlat(admin.ModelAdmin):

    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('active', 'new_building', 'rooms_number', 'has_balcony', 'floor',)
    search_fields = ['town', 'address', 'construction_year', 'id']
    raw_id_fields = ('liked_by',)
    readonly_fields = ['created_at', ]
    inlines = [OwnersInline]
    fieldsets = (
        ('Статус',
         {'fields': ('active', 'new_building')}
         ),
        ('Адрес',
         {'fields': (('town', 'town_district'), 'address')}
         ),
        ('Общее',
         {'fields': ('construction_year', 'created_at')}
         ),
        ('Квартира',
         {'fields': ('rooms_number', 'has_balcony', 'floor', 'living_area', 'liked_by', 'price', 'description')}
         )
        )
    list_per_page = 20
    

@admin.register(Complaint)
class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ('user', 'apartments')
    search_fields = ('user__username',)


@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    raw_id_fields = ('apartments',)
    search_fields = ('owner', 'apartments__id', 'apartments__town')
