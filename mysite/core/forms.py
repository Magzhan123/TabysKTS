# -*- coding: utf-8 -*-
from django import forms

class ProductForm(forms.Form):
  title = forms.CharField(label='Product title')
  price = forms.IntegerField(label='Price')
  short_desc = forms.CharField(label='Product short desc ')
  full_desc = forms.CharField(label='Product full desc ')
  category = forms.CharField(label='Product category ')
  brand = forms.CharField(label='Brand')
  main_image = forms.ImageField(label='Image')

class PostForm(forms.Form):
  title = forms.CharField(label='Product title')
  body = forms.CharField(label='Product short desc ')
  main_image = forms.ImageField(label='Image')