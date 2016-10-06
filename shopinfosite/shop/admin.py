from django.contrib import admin

# Register your models here.

from .models import Category, Item, ItemImage, About
from .models import Contact, ContactMessage, Gallery, BannerImage, News , GalleryImage , ShopLogo


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(ContactMessage)
admin.site.register(Gallery)
admin.site.register(BannerImage)
admin.site.register(News)
admin.site.register(GalleryImage)
admin.site.register(ShopLogo)
