
from .models import Category, ShopLogo,SocialLink, Item, News, About,Contact


def categories(request):

    return {
        'categories': Category.objects.all(),
    }


def shop_logo(request):

    try:


        return {
            'logo': ShopLogo.objects.latest('created_at'),
        }
    except:

        return {
            'logo': False
        }


def social_links(request):
    try:

        return {
            'social_links': SocialLink.objects.latest('created_at'),
        }
    except:

        return {
            'social_links': False
        }


def latest_items(request):

    try:

        return {
            'latest_items': Item.objects.lorder_by("-date")[:5]
        }
    except:
        return {
            'latest_items': False
        }


def recent_news(request):
    try:

        return {
            'recent_news': News.objects.latest('created_at')
        }
    except:
        return {
            'recent_news': False
        }


def about_us(request):
    try:

        return {
            'about_us': About.objects.latest('created_at')
        }
    except:
        return {
            'about_us': False
        }
def contact_us(request):
    try:

        return {
            'contact_us': Contact.objects.latest('created_at')
        }
    except:
        return {
            'contact_us': False
        }
