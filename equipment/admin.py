from django.contrib import admin
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _
from django.core.validators import EMPTY_VALUES

from unfold.admin import ModelAdmin, TabularInline
from unfold.decorators import display

from .models import Equipment, DMEOrder, DMEOrderItem
from .forms import DMEOrderItemFormSet, DMEOrderForm, DMEOrderItemForm

@admin.register(Equipment)
class EquipmentAdmin(ModelAdmin):
    warn_unsaved_form = True  # Default: False
    list_disable_select_all = True 
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    list_display = ["name", "stock", "barcode"]
    search_fields = ["name", "barcode"]
    list_filter = ["stock", "name"]

class OrderItemInline(TabularInline):
    model = DMEOrderItem
    formset = DMEOrderItemFormSet
    extra = 0
    can_delete = True
    autocomplete_fields = ["equipment"]
    verbose_name = "Equipment Associated with Order"
    verbose_name_plural = "Equipment Associated with Order"


class OrderStatuc(TextChoices):
    RENTED = "RT", _("Rented")
    RETURNED = "RU", _("Returned")

@admin.register(DMEOrder)
class OrderAdmin(ModelAdmin):
    form = DMEOrderForm
    inlines = [OrderItemInline]
    warn_unsaved_form = True  # Default: False
    list_disable_select_all = True 
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    list_display = ["client","client_phone", "equipment", "client_area_serviced_name", "show_status_customized_color"]
    list_filter = ["status", "items__equipment", "client__area_serviced__name", "client__area_serviced__name"]
    list_display_links = ["client", "show_status_customized_color"]
    search_fields = ["client__name", "client__phone", "items__equipment__name", "status", "client__area_serviced__name"]
    autocomplete_fields = ["client"]
    verbose_name = "DME Order"
    verbose_name_plural = "DME Orders"
    
    @display(
        description=_("Status"),
        ordering="status",
        label=True
    )
    def show_status_default_color(self, obj):
        return obj.status

    @display(
        description=_("Status"),
        ordering="status",
        label={
            'Rented' : "danger",
            'Returned' : "success"
        },
    )
    def show_status_customized_color(self, obj):
        if obj.status == OrderStatuc.RENTED:
            return 'Rented'
        return 'Returned'

    @display(
        description=_("Equipment Rented"),
        ordering="equipment",
        label=True
    )
    def equipment(self, obj):
        items = DMEOrderItem.objects.filter(order=obj)
        return ", ".join([f"{item.equipment.name} ({item.quantity})" for item in items])


    @display(
        description=_("Client Area Serviced"),
        ordering="client__area_serviced__name",
        label=True
    )
    def client_area_serviced_name(self, obj):
        if obj.client and obj.client.area_serviced:
            return obj.client.area_serviced.name
        return None

    @display(
        description=_("Client Phone"),
        ordering="client__phone",
        label=True
    )
    def client_phone(self, obj):
        if obj.client:
            return obj.client.phone
        return None
    
@admin.register(DMEOrderItem)
class DMEOrderItemAdmin(ModelAdmin):
    warn_unsaved_form = True
    list_display = ["equipment", "quantity"]
    autcomplete_fields = ["equipment"]
    search_fields = ["equipment"]

