from django.db import models
from django.db.models import Q
from django.core.files.base import ContentFile
from django.core.files import File
from django.core.files.storage import default_storage
from django.conf import settings
import uuid
import os

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Feature(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    renting = models.ForeignKey("renting.Renting", on_delete=models.CASCADE, related_name='renting_images')
    image = models.ImageField(upload_to='renting/images')
    is_first = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.renting.title} - {self.id} image"


class Renting(models.Model):
    title = models.CharField(max_length=200)
    uuid = models.UUIDField(unique=True, editable=False, db_index=True, verbose_name='Public ID', default=uuid.uuid4)
    owner = models.ForeignKey("account.User", on_delete=models.CASCADE, related_name='renting_owner')
    description = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    full_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    square_meter = models.CharField(max_length=5)
    price = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='rent_type')
    feautes = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='rent_features')
    is_active = models.BooleanField(default=True)
    is_approve = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def create_renting(self, title, description, city, state, full_address, phone, square_meter, price, type_id, feautes, owner, images):
        response = Renting.objects.create(
            title=title, 
            description=description, 
            city=city, 
            state=state, 
            full_address=full_address, 
            phone=phone, 
            square_meter=square_meter, 
            price=price, type_id=type_id, 
            feautes_id=feautes, 
            owner=owner)
        # create image
        for index, image_file in enumerate(images):
            is_first = index == 0
            img_name = f"image_{response.id}_{index}.png"  # Modify as per your naming convention
            image_obj = Image(renting=response, is_first=is_first)
            
            # Use Django's File class to save the image
            image_obj.image.save(img_name, File(image_file), save=True)
        return response
    
    def update_renting(self, title, description, city, state, full_address, phone, square_meter, price, type_id, feautes, owner, images, pk):
        response = Renting.objects.filter(uuid=pk).update(
            title=title, 
            description=description, 
            city=city, 
            state=state, 
            full_address=full_address, 
            phone=phone, 
            square_meter=square_meter, 
            price=price, type_id=type_id, 
            feautes_id=feautes, 
            owner=owner)

        # delete old images
        instance = Renting.objects.get(uuid=pk)
        # create image
        prev_images = instance.get_images()
        if len(prev_images) == 0:
            for index, image_file in enumerate(images):
                is_first = index == 0
                img_name = f"image_{instance.id}_{index}.png"
                image_obj = Image(renting=instance, is_first=is_first)
                image_obj.image.save(img_name, File(image_file), save=True)
        else:
            for index, image_file in enumerate(images):
                img_name = f"image_{instance.id}_{index}.jpg"  # Modify as per your naming convention
                image_obj = Image(renting=instance, is_first=False)
                # Use Django's File class to save the image
                image_obj.image.save(img_name, File(image_file), save=True)
        return response
    
    def delete_renting(self, pk, user_id):
        response = Renting.objects.filter(uuid=pk)[0]
        if (user_id == response.owner.id):
            response.delete()
            return True
        else:
            return False

    def get_paginated_renting(self, page):
        offset = (page - 1) * 6
        limit = offset + 6
        response = Renting.objects.all()[offset:limit]
        return response
    
    def get_count_renting(self):
        response = Renting.objects.all().count()
        return response
    
    def get_searched_renting(self, search):
        response = Renting.objects.filter(
            Q(title__icontains=search) | 
            Q(city__icontains=search) | 
            Q(state__icontains=search))
        return response


    def filter_renting(self, rent_type, features, min_price, max_price):
        filters = Q()  # Initialize an empty query
        
        if rent_type:
            filters &= Q(type__id__in=rent_type)
        
        if features:
            filters &= Q(feautes__id__in=features)
        
        if min_price:
            filters &= Q(price__gte=min_price)
        
        if max_price:
            filters &= Q(price__lte=max_price)
        
        if not any([rent_type, features, min_price, max_price]):
            return Renting.objects.all()  # Return all if no filters applied
        
        response = Renting.objects.filter(filters)
        return response

    
    def get_images(self):
        response = Image.objects.filter(renting=self)
        return response



class Favorite(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.CASCADE, related_name='favorite_user')
    renting = models.ForeignKey(Renting, on_delete=models.CASCADE, related_name='favorite_renting')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.renting.uuid}"    
    
    def create_favorite(self, user, renting):
        response = Favorite.objects.create(user=user, renting=renting)
        return response
    
    def delete_favorite(self, user, renting):
        response = Favorite.objects.filter(user=user, renting=renting).delete()
        return response
    
    def get_favorite(self, user, renting):
        response = Favorite.objects.filter(user=user, renting=renting)
        return response
    
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    meta_description = models.CharField(max_length=1000)
    meta_keywords = models.CharField(max_length=1000)
    author = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def create_tag(self, name, meta_description, meta_keywords):
        response = Tag.objects.create(name=name, meta_description=meta_description, meta_keywords=meta_keywords)
        return response
    
    def update_tag(self, description, keywords, author, pk):
        response = Tag.objects.filter(id=pk).update(meta_description=description, meta_keywords=keywords, author=author)
        return response




