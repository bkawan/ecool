from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
import smtplib
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from email.mime.text import MIMEText
from .models import Category, Contact, News, About, Item, BannerImage, Gallery, GalleryImage, ItemImage
from django.http import HttpResponse
import requests
from django.shortcuts import render_to_response, get_object_or_404
from .forms import ContactForm
from django.conf import settings

if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail
from django.core import mail


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
    return render(request, 'about.html', context)


def contact(request):
    form_class = ContactForm

    context = {
        'contacts': Contact.objects.all(),
        'form': form_class,
        'abouts': About.objects.all(),
        'banners': BannerImage.objects.all(),

    }

    if request.method =='POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            # full_name = request.POST.get(
            #     'full_name',
            #     ''
            # )
            # contact_no = request.POST.get(
            #     'contact_no',
            #     ''
            # )
            # email = request.POST.get(
            #     'email',
            #     ''
            # )
            # message = request.POST.get(
            #     'message',
            #     ''
            # )
            #


            form.save()
            messages.add_message(request, messages.SUCCESS, "Your message has been sucessfully sent.!! Thank you")
            return HttpResponseRedirect('/')
        else:
            return render(request, 'contact.html', {'form': form})

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
        # 'items': Item.objects.filter(category=category),
        'latest_item_in_category': Item.objects.filter(category=category).latest('created_at'),
    }

    # return render(request, 'category.html', context)
    return render(request, 'view_category.html', context)


def view_category_product(request, category_id, item_id):
    item = get_object_or_404(Item, pk=item_id)
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'category': category,
        'item': item,
        'latest_item_in_category': Item.objects.filter(category=category).latest('created_at'),
    }

    # return render(request, 'category.html', context)
    return render(request, 'view_category.html', context)


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

    return render(request, 'products.html', {'products': products}, )


def view_product(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        "categories": Category.objects.all(),
        "product": item,
        "item_images": ItemImage.objects.filter(item=item),

    }

    return render(request, template_name='view_product.html', context=context)



def send_simple_message(full_name,sender,message):
    return requests.post(
        "https://api.mailgun.net/v3/effectivecool.com",
        auth=("api", "key-8df30a190b4f08d61f09c13630f2491c"),
        data={"from": "postmaster@effectivecool.com",
              "to": ["bikeshkawang@gmail.com"],
              "subject": full_name,
              "text": message})



from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

def reset_confirm(request, uidb36=None, token=None):
    return password_reset_confirm(request, template_name='app/reset_confirm.html',
        uidb36=uidb36, token=token, post_reset_redirect=reverse('app:login'))


def reset(request):
    return password_reset(request, template_name='app/reset.html',
        email_template_name='app/reset_email.html',
        subject_template_name='app/reset_subject.txt',
        post_reset_redirect=reverse('app:login'))