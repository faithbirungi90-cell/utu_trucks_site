from django.contrib import admin
from .models import TruckCategory, TruckModel, TruckImage, QuoteRequest

# Inline gallery editor for uploading multiple images inside a single truck page
class TruckImageInline(admin.TabularInline):
    model = TruckImage
    extra = 3  # Gives 3 empty photo upload slots by default

@admin.register(TruckCategory)
class TruckCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(TruckModel)
class TruckModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'range_km', 'payload_capacity_kg', 'battery_capacity_kwh', 'featured')
    list_filter = ('category', 'featured')
    search_fields = ('name', 'tagline')
    inlines = [TruckImageInline]

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company_name', 'email', 'phone', 'truck_model', 'created_at')
    readonly_fields = ('created_at',)
    search_fields = ('full_name', 'company_name', 'email', 'phone')