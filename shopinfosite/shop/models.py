from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(
        auto_now=True, editable=False)

    name = models.CharField(max_length=255, null=True,blank=True)
    slug = models.SlugField(max_length=100, unique=True)


    class Meta:
        verbose_name_plural = _("Categories")
        db_table = 'categories'
    #
    # def __unicode__(self):
    #
    #     return force_unicode(self.name)


    def __str__(self):
        return self.name


class Item(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(
        auto_now=True, editable=False)

    name = models.CharField(max_length=255, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    descriptions = models.TextField(null=True, blank=True)
    item_logo = models.FileField(upload_to='images/item_logo/', null=True, blank=True)

    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        db_table = 'items'

    # def __unicode__(self):
    #     return force_unicode(self.name)
    #

    def __str__(self):

        return self.name


class ItemImage(models.Model):

    image = models.FileField(upload_to='images/item_images/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


    class Meta:
        db_table = 'item_images'
    #
    # def __unicode__(self):
    #     return force_unicode(self.title)

    def __str__(self):
        return self.image


class Contact(models.Model):

    company_name = models.CharField(max_length=255, null=True, blank=True)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    zone = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    telephone_no = models.PositiveIntegerField(null=True, blank=True)
    mobile_no = models.PositiveIntegerField(null=True, blank=True)
    fax = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    googleplus = models.CharField(max_length=255, null=True, blank=True)

    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        db_table = 'contacts'

    # def __unicode__(self):
    #     return force_unicode(self.company_name)
    #


class Gallery(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(
        auto_now=True, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    cover_image = models.ImageField(upload_to='images/galleries/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        db_table = "galleries"

    # def __unicode__(self):
    #     return force_unicode(self.company_name)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='images/galleries/', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    class Meta:
        db_table = 'gallery_images'

    def __str__(self):
        return self.image.url



class About(models.Model):

    short_info = models.TextField(null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)



    class Meta:
        db_table = 'abouts'
    #
    # def __unicode__(self):
    #     return force_unicode(self.company_name)

    def __str__(self):
        return self.short_info


class ContactMessage(models.Model):

    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    contact_no = models.PositiveIntegerField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

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

        return self.name + ": " + self.image.url


class News(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(
        auto_now=True, editable=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'news'

    def __str__(self):
        return self.title


class ShopLogo(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(
        auto_now=True, editable=False)
    logo = models.ImageField(upload_to="images/shop_logo")
    title = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        db_table = 'shop_logos'

    def __str__(self):
        return self.title + ":" + self.logo.url
