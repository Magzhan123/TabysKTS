from django.contrib import admin

from .models import Product
from .models import Post

class ProductAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "added"]

admin.site.register(Product, ProductAdmin)


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)