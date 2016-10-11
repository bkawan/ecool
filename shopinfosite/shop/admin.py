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
        'message',
    )
    list_display = (
            'full_name',
            'email',
            'contact_no',
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
admin.site.register(Item, ItemCoverImageProfile)


class ItemImageProfile(admin.ModelAdmin):
    readonly_fields = (
        'item_image',
    )
    list_display = ('item', 'image_name', 'item_image')

admin.site.register(ItemImage, ItemImageProfile)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(ContactMessage, ContactMessageProfile)
admin.site.register(Gallery, ImageNameProfile)
admin.site.register(BannerImage)
admin.site.register(News)
admin.site.register(GalleryImage, ImageNameProfile)
admin.site.register(ShopLogo)


class SocialLinkProfile(admin.ModelAdmin):

    list_display = ('facebook', 'twitter', 'googleplus', 'youtube', 'linkedin')
admin.site.register(SocialLink, SocialLinkProfile)
