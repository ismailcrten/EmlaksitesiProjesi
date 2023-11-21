from django.contrib import admin
from emlak.models import Category, Emlak , Images

class EmlakImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["tittle", "status"]
    list_filter = ["status"]


# Register your models here.
class EmlakAdmin(admin.ModelAdmin):
    list_display = ["tittle", "category", "price","image_tag","status" ]
    readonly_fields = ("image_tag",)
    list_filter = ["status"]
    inlines = [EmlakImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ["title", "emlak", "image"]
    list_filter = ["emlak"]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ["title", "emlak","image"]
    readonly_fields = ("image_tag",)
    list_filter = ["emlak"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Emlak, EmlakAdmin)
admin.site.register(Images, ImagesAdmin)