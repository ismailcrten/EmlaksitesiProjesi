from django.contrib import admin
from emlak.models import Category
class CategoryAdmin(admin.ModelAdmin):
   list_display  = ["tittle", "status"]
   list_filter = ["status"]
# Register your models here.


admin.site.register(Category, CategoryAdmin)