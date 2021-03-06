from django.db import models
from django.utils.translation import ugettext_lazy as _
import os
# Create your models here.
from django.utils.safestring import mark_safe

from ckeditor.fields import RichTextField
from django.core.validators import validate_email
class Category(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True, editable=True)
    modified_at = models.DateTimeField(
        auto_now=True, editable=True)

    name = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=100, unique=True)


    class Meta:
        verbose_name_plural = _("Categories")
        db_table = 'categories'
    #
    # def __unicode__(self):
    #
    #     return force_unicode(self.name)


    def __str__(self):
        return self.name

    def get_products(self):
        return Item.objects.filter(category=self)



class Item(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True, editable=True)
    modified_at = models.DateTimeField(
        auto_now=True, editable=True)

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # descriptions = models.TextField(null=True, blank=True)
    descriptions = RichTextField()
    item_logo = models.FileField(upload_to='images/item_logo/')

    # slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        db_table = 'items'

    # def __unicode__(self):
    #     return force_unicode(self.name)
    #

    def __str__(self):

        return self.name

    def item_cover_image(self):
        return '<img src="{}" height="40px" width="40px"/>'.format(self.item_logo.url)

    item_cover_image.allow_tags = True

    def get_images(self):
        return ItemImage.objects.filter(item=self)

    def image_name(self):
        return os.path.basename(self.item_logo.name)


class ItemImage(models.Model):

    # slug = models.SlugField(max_length=100, unique=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='images/item_images/')



    class Meta:
        db_table = 'item_images'
    #

    def __str__(self):
        return self.image.url

    def item_image(self):
        return '<img src="{}" height="100px" width="100px"/>'.format(self.image.url)

    item_image.allow_tags = True

    def image_name(self):
        return os.path.basename(self.image.name)


class Contact(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=True)
    modified_at = models.DateTimeField(
        auto_now=True, editable=True)

    company_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255, null=True, blank=True)
    zone = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255)
    telephone_no = models.PositiveIntegerField()
    mobile_no = models.PositiveIntegerField()
    fax = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255)

    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    googleplus = models.CharField(max_length=255, null=True, blank=True)

    # slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        db_table = 'contacts'

    # def __unicode__(self):
    #     return force_unicode(self.company_name)
    #


class Gallery(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True, editable=True)
    modified_at = models.DateTimeField(
        auto_now=True, editable=True)
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='images/galleries/')
    # slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        db_table = "galleries"

    # def __unicode__(self):
    #     return force_unicode(self.company_name)

    def __str__(self):
        return self.name

    def image_name(self):
        return os.path.basename(self.cover_image.name)

    def gallery_image(self):
        return '<img src="{}" height="100px" width="100px"/>'.format(self.cover_image.url)

    gallery_image.allow_tags = True


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='images/galleries/')
    name = models.CharField(max_length=255, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    class Meta:
        db_table = 'gallery_images'

    def __str__(self):
        return self.image.url

    def image_name(self):
        return os.path.basename(self.image.name)

    def gallery_image(self):
        return '<img src="{}" height="100px" width="100px"/>'.format(self.image.url)

    gallery_image.allow_tags = True



class About(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=True)
    modified_at = models.DateTimeField(
        auto_now=True, editable=True)

    company_name = models.CharField(max_length=255, null=True, blank=True)
    short_info = RichTextField()
    descriptions = RichTextField()
    # slug = models.SlugField(max_length=100, unique=True)


    class Meta:
        db_table = 'abouts'
    #
    # def __unicode__(self):
    #     return force_unicode(self.company_name)

    def __str__(self):
        return self.company_name


class ContactMessage(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact_no = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        db_table = 'contact_messages'

    def __str__(self):
        return self.full_name


class BannerImage(models.Model):

    image = models.ImageField(upload_to="images/banners/")
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'banner_images'

    def __str__(self):

        # return self.name + ": " + self.image.url
        return os.path.basename(self.image.name)

    def banner_image(self):
        return '<img src="{}" height="100px" width="100px"/>'.format(self.image.url)


    banner_image.allow_tags = True

    def banner_image_base_name(self):
        return os.path.basename(self.image.name)


class News(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=True)
    modified_at = models.DateTimeField(
        auto_now=True, editable=True)
    title = models.CharField(max_length=255)
    descriptions = RichTextField()

    class Meta:
        db_table = 'news'

    def __str__(self):
        return self.title


class ShopLogo(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=True)
    modified_at = models.DateTimeField(
        auto_now=True, editable=True)
    logo = models.ImageField(upload_to="images/shop_logo")
    title = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        db_table = 'shop_logos'

    def __str__(self):
        return self.title + ":" + self.logo.url

    def logo_image(self):
        return '<img src="{}" height="100px" width="100px"/>'.format(self.logo.url)

    logo_image.allow_tags = True


class SocialLink(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=True)
    modified_at = models.DateTimeField(
        auto_now=True, editable=True)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    googleplus = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'social_links'

    def __str__(self):
        return self.facebook
