from django.contrib import admin
from .models import (
    Hotel,
    HotelStatus,
    HotelChain,
    HotelRoom,
    ContractManager,
    SalesContact,
    HotelTag,
)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "chain",
        "country",
        "region",
        "area",
        "latitude",
        "longitude",
        "contract_manager",
        "sales_contact",
        "giata",
        "get_tags",
        "updated_at",
        "updated_by",
        "status",
    )
    list_filter = ("area__region__country", "area__region", "area", "chain", "status", "contract_manager")
    list_per_page = 20
    search_fields = ("id", "name", "giata", "chain__name")
    # inlines = (
    #     HotelMappingInline,
    #     HotelRoomInline,
    # )
    fieldsets = (
        ("General Information", {"fields": ("name", "category", "chain")}),
        ("Location", {"fields": ("area", "latitude", "longitude")}),
        ("Contacts", {"fields": ("sales_contact", "contract_manager")}),
        ("Additional Information", {"fields": ("status", "tags", "giata")}),
    )

    raw_id_fields = ("area", "tags", "sales_contact")
    autocomplete_lookup_fields = {
        "fk": ["area", "sales_contact"],
        "m2m": ["tags"],
    }

    def country(self, obj):
        try:
            return obj.area.region.country
        except AttributeError:
            return None

    def region(self, obj):
        try:
            return obj.area.region.name
        except AttributeError:
            return None

    @admin.display(description="Tags")
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    def save_model(self, request, obj, form, change):
        if not obj.id:  # New hotel creation
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(SalesContact)
class SalesContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "designation", "email", "mobile")
