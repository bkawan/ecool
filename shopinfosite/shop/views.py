from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from .models import Category, Contact, News, About, Item, BannerImage, Gallery, GalleryImage, ItemImage
from django.http import HttpResponse

from django.shortcuts import render_to_response, get_object_or_404
from .forms import ContactForm


def index(request):
    context = {
        # 'categories': Category.objects.all(),
        'contacts': Contact.objects.all(),
        'abouts': About.objects.all(),
        # 'newses': News.objects.all(),
        'newses': News.objects.order_by("-created_at")[:1],
        # 'items': Item.objects.all(),
        'items': Item.objects.order_by("-created_at")[:5],
        'banners': BannerImage.objects.all(),


    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        # 'categories': Category.objects.all(),
        'contacts': Contact.objects.all(),
        'abouts': About.objects.all(),

    }
    return render(request,'about.html', context)

def contact(request):
    form_class = ContactForm

    context = {
        'contacts': Contact.objects.all(),
        'form': form_class,
        'abouts': About.objects.all(),
        'banners': BannerImage.objects.all(),

    }

    return render(request, 'contact.html', context)


# def contactMessage(request):
#     form_class = ContactForm
#
#     return render(request, 'contact.html', {
#         'form': form_class,
#     })


def view_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'category': category,
        'items': Item.objects.filter(category=category),
        'latest_item': Item.objects.filter(category=category).latest('created_at'),
    }

    return render(request, 'category.html', context)


def galleries(request):

    context = {
        'galleries': Gallery.objects.all(),
    }

    return render(request, template_name='gallery.html', context=context)


def view_gallery(request, gallery_id):

    gallery = get_object_or_404(Gallery, pk=gallery_id)
    context = {
        "gallery": gallery,
        "gallery_images": GalleryImage.objects.filter(gallery=gallery),

    }

    return render(request, template_name='view_gallery.html', context=context)


def news(request):
    context = {
        'news': News.objects.all(),
    }
    return render(request, template_name='news.html', context=context)


def products(request):
    product_list = Item.objects.all()
    paginator = Paginator(product_list, 20)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'products.html', {'products': products},)



def view_product(request,item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        "categories": Category.objects.all(),
        "product": item,
        "item_images": ItemImage.objects.filter(item=item),


    }

    return render(request, template_name='view_product.html', context=context)

