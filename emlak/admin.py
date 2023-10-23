from django.contrib import admin
from emlak.models import Category, Emlak


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["tittle", "status"]
    list_filter = ["status"]


# Register your models here.
class EmlakAdmin(admin.ModelAdmin):
    list_display = ["tittle", "category", "price", "status"]
    list_filter = ["status"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Emlak, EmlakAdmin)
