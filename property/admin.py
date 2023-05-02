from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersInline(admin.TabularInline):
    model = Owner.addresses.through
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


@admin.register(Complaint)
class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ('user', 'address')
    search_fields = ('user__username',)


@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    raw_id_fields = ('addresses',)
    search_fields = ('owner', 'addresses__id', 'addresses__town')
