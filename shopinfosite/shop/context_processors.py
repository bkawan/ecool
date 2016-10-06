
from .models import Category, ShopLogo


def categories(request):

    return {
        'categories': Category.objects.all(),
    }


def shop_logo(request):

    return {
        'logo': ShopLogo.objects.latest('created_at'),
    }

