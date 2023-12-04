# Create your models here.
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ("True", "Evet"),
        ("False", "Hayır"),
    )
    tittle = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    image=models.ImageField(blank=True, upload_to="images/")
    status=models.CharField(max_length=10, choices=STATUS)
    slug=models.SlugField()
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children", on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.tittle


class Emlak(models.Model):
    STATUS = (
        ("True", "Evet"),
        ("False", "Hayır"),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    image=models.ImageField(blank=True, upload_to="images/")
    price= models.FloatField()
    amount = models.IntegerField()
    detail= RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug=models.SlugField(blank=True, null=False)

    def __str__(self):
        return self.tittle

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Images(models.Model):
    emlak = models.ForeignKey(Emlak, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,)
    image=models.ImageField(blank=True, upload_to="images/")
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'