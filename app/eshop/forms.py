from django import forms
from eshop.models import Product
from eshop.models import Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'image')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('author', 'description', 'score')