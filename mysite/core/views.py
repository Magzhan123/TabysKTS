# -*- coding: utf-8 -*-
import os
from django.db.models import Q
from django.shortcuts import render,redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings
from models import Product
from forms import ProductForm, PostForm
from models import Post
from django.core.urlresolvers import reverse

import img_utils

def main(request):
    """Main listing."""
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, "core/postt.html", {'posts': posts, 'user': request.user})

def about(request):
    return render(request, "core/about.html", {})

def login(request):
    return render(request, "core/login.html", {})

def contact(request):
    return render(request, "core/contact.html", {})

def activations(request):
    return render(request, "core/activations.html", {})

def register(request):
    return render(request, "core/register.html", {})

def checkout(request):
    return render(request, "core/checkout.html", {})

def product(request):
    # filters = {
    #     "category__iexact": "",
    #     "price": "",
    #     "brand": "",
    # }
    order_by = request.GET.get('sort', '-added')
    # products = Product.objects.all()
    # for filter in filters:
    #     temp = request.GET.get(filter, '')
    #     if temp:
    #         temp_filter = temp.split(',')
    #         statemant = {filter + '__contains': }
    #         products = products.filter(
    #             reduce(
    #                 operator.and_, 
    #                 (Q(brand__contains=x) for x in ['x', 'y', 'z'])))
    #         new_filters[filter] = temp
    # products = Product.objects.filter(
    #     reduce(
    #         operator.and_, 
    #         (Q(brand__contains=x) for x in ['x', 'y', 'z'])))
    products = Product.objects.order_by(order_by)
    # print products
    response = {
        'categories': ['Камеры', 'Антирадары'],
        'brands': ['Nikon', 'Canon', 'Fujitsu'],
        'products': products,
        'order_by': order_by
    }
    return render(request, "core/product.html", response)

def switch_lang(request):
    request.session['lang'] = request.GET.get('lang', 'ru')
    next_page = request.GET.get('next', 'index')
    print next_page
    return redirect(next_page)

def home_page(request):
    lang = request.session.get('lang', 'ru')
    products = Product.objects.all()
    return render(request, "core/" + lang + "/home_page.html", {"products": products})

def uslug(request):
    return render(request, "core/uslug.html", {})

def blogs(request):
    post = Post.objects.all()
    paginator
    return render(request, "core/postt.html", {"posts" : post})

def single(request):
    return render(request, "core/single.html", {})

def test(request):
    products = Product.objects.all()
    product = ProductForm()
    return render(request, "core/test.html", {"products": products, "product": product})

def create_product(request):
  kwargs = {}
  for k in request.POST:
    if k != 'csrfmiddlewaretoken':
      kwargs[k] = request.POST[k]
  product =  Product(**kwargs)
  product.save()
  for k in request.FILES:
    filename = img_utils.thumb_image('main_image', str(product.pk), request.FILES[k], (300, 273))
    setattr(product, k, filename)
  product.save()

def admin_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            create_product(request)
        else:
            print form.errors
    if not request.user or not request.user.is_staff:
        return redirect('login')
    categories = ['Камеры', 'Антирадары']
    brands = ['Nikon', 'Canon', 'Fujitsu']
    return render(request, "core/admin/index.html", {"categories": categories, "brands": brands})

def create_post(request):
  kwargs = {}
  for k in request.POST:
    if k != 'csrfmiddlewaretoken':
      kwargs[k] = request.POST[k]
  post =  Post(**kwargs)
  post.save()
  for k in request.FILES:
    filename = img_utils.thumb_image('post_image', str(post.pk), request.FILES[k], (300, 273))
    setattr(post, k, filename)
  post.save()


def admin_posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            create_post(request)
        else:
            print form.errors
    if not request.user or not request.user.is_staff:
        return redirect('login')
    return render(request, "core/admin/news.html")