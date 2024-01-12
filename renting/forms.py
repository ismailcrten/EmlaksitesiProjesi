from django import forms
from django import forms
from renting.models import Type, Feature

class FilterForm(forms.Form):
    TYPES_CHOICES = [(type.id, type.name) for type in Type.objects.all()]
    FEATURES_CHOICES = [(feature.id, feature.name) for feature in Feature.objects.all()]
    

    types = forms.MultipleChoiceField(
        choices=TYPES_CHOICES, 
        widget=forms.CheckboxSelectMultiple, 
        label='Kiralama Türü',
        required=False,
        template_name='renting/filter_form.html')
    features = forms.MultipleChoiceField(
        choices=FEATURES_CHOICES, 
        widget=forms.CheckboxSelectMultiple, 
        label='Özellikler',
        required=False)
    price_range_min = forms.IntegerField(
        label='Min Fiyat',
        required=False)
    price_range_max = forms.IntegerField(
        label='Max Fiyat',
        required=False)

