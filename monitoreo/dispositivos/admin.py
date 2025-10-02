
from django.contrib import admin
from .models import (
 Category, Product, AlertRule, ProductAlertRule,
 Zone, Device, Measurement, AlertEvent
)
# ─────────────────────────────────────────────────────────
# Reglas generales del sitio (opcional, pero queda bonito)
# ─────────────────────────────────────────────────────────
admin.site.site_header = "EcoEnergy — Admin"
admin.site.site_title = "EcoEnergy Admin"
admin.site.index_title = "Panel de administración"
# ─────────────────────────────────────────────────────────
# MAESTROS (globales)
# ─────────────────────────────────────────────────────────
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
# Columnas que se ven en la lista
list_display = ("name", "status", "created_at")
# Campos por los que se puede buscar
search_fields = ("name",)
 # Filtros de la derecha
 list_filter = ("status",)
 # Orden por defecto
 ordering = ("name",)
# Filas por página (opcional)
 list_per_page = 50

# Register your models here.

from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "role")
    search_fields = ("user__username", "organization__name", "role")

