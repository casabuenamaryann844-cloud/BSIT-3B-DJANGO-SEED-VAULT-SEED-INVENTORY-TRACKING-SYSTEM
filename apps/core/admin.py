from django.contrib import admin
from .models import SeedInventory


@admin.register(SeedInventory)
class SeedInventoryAdmin(admin.ModelAdmin):
    list_display = (
        'seed_name',
        'variety',
        'category',
        'quantity',
        'unit',
        'storage_location',
        'expiration_date',
    )
    search_fields = ('seed_name', 'variety', 'storage_location')
    list_filter = ('category', 'unit')
    ordering = ('seed_name',)
