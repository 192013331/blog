from django import forms
from sympy.categories import Category


class PubBlogForm(forms.Form):
    title = forms.CharField(max_length=200,min_length=2)
    content = forms.CharField(min_length=2)
    category = forms.IntegerField()
