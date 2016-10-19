from django.contrib import admin

# Register your models here.

from .models import Category, Item, ItemImage, About
from .models import Contact, ContactMessage, Gallery
from .models import BannerImage, News, GalleryImage, ShopLogo, SocialLink


class DateProfile(admin.ModelAdmin):
    readonly_fields = ['created_at', 'modified_at']


class ContactMessageProfile(admin.ModelAdmin):
    readonly_fields = (
        'full_name',
        'email',
        'contact_no',
        'title',
        'message',
        'created_at',
    )
    list_display = (
        'full_name',
        'email',
        'contact_no',
        'title',
        'created_at',
    )


class ItemCoverImageProfile(admin.ModelAdmin):
    readonly_fields = (
        'item_cover_image',
    )
    list_display = ('name', 'category', 'item_cover_image',)


class ImageNameProfile(admin.ModelAdmin):
    readonly_fields = (
        'image_name',
    )
    list_display = ('image_name',)

admin.site.register(Category, DateProfile)


class ItemProfile(admin.ModelAdmin):
    search_fields = ['name', 'descriptions']
    readonly_fields = (
        'item_cover_image',
    )
    list_display = ('name', 'category', 'item_cover_image',)


admin.site.register(Item, ItemProfile)


class ItemImageProfile(admin.ModelAdmin):
    readonly_fields = (
        'item_image',
    )
    list_display = ('item_image', 'item', 'image_name', )


admin.site.register(ItemImage, ItemImageProfile)

admin.site.register(About)


class ContactProfile(admin.ModelAdmin):
    readonly_fields = ['created_at', 'modified_at']
    list_display = ('company_name', 'email', 'street_address')
admin.site.register(Contact, ContactProfile)
admin.site.register(ContactMessage, ContactMessageProfile)


class GalleryProfile(admin.ModelAdmin):
    readonly_fields = ('image_name', 'gallery_image')
    list_display = ('gallery_image', 'name', 'image_name')
admin.site.register(Gallery, GalleryProfile)


class BannerImageProfile(admin.ModelAdmin):
    readonly_fields = (
        'banner_image',
    )
    list_display = ('banner_image', 'banner_image_base_name', 'name')
admin.site.register(BannerImage, BannerImageProfile)


class NewsProfile(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ['title', 'description']
    list_display = ('title', 'created_at')

admin.site.register(News, NewsProfile)


class GalleryImageProfile(admin.ModelAdmin):
    readonly_fields = (
        'image_name', 'gallery_image',
    )
    list_display = ('gallery_image',  'gallery', 'image_name', 'name',)

admin.site.register(GalleryImage, GalleryImageProfile)

class ShopLogoProfile(admin.ModelAdmin):
    readonly_fields = (
        'logo_image', 'created_at', 'modified_at',
    )
    list_display = ('logo_image','title')
admin.site.register(ShopLogo, ShopLogoProfile)


class SocialLinkProfile(admin.ModelAdmin):
    list_display = ('facebook', 'twitter', 'googleplus', 'youtube', 'linkedin')


admin.site.register(SocialLink, SocialLinkProfile)


