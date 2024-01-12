from django.contrib import admin
from renting.models import Type, Feature, Renting, Image, Favorite, Tag
# Register your models here.

admin.site.register(Type)
admin.site.register(Feature)
admin.site.register(Renting)
admin.site.register(Image)
admin.site.register(Favorite)
admin.site.register(Tag)

