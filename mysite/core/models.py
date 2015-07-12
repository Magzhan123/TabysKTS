from django.utils import translation

from django.db import models

class Product(models.Model):

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    title = models.CharField(max_length=50)
    price = models.IntegerField()
    short_desc = models.TextField()
    full_desc = models.TextField()
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    main_image = models.CharField(max_length=512)
    added = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.title, str(self.price))
    

class Post(models.Model):

    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    main_image = models.CharField(max_length=512, null=True)


    def __unicode__(self):
        return self.title