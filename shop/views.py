from .recommender import Recommender
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import ContactForm
from django.core.mail import send_mail

def index(request):
    return render(request, 'shop/index.html',{})

def contact(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "DSG {}".format(cd['subject'])
            message = "DSG Support request from {} {}({})\n\n{}\n DSG Contact Form".format(cd['fname'], cd['lname'], cd['email'], cd['message'])
            send_mail(subject, message, 'noreply@deut818systems.com', 'contact@deut818systems.com')
            form.save()
            sent = True
    return render(request, 'shop/contact.html', {'form':form, 'sent':sent})

def about(request):
    return render(request, 'shop/about.html', {})

def privacy(request):
    return render(request, 'shop/privacy.html', {})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    sort_10 = Product.objects.filter(available=True)[:10]
    sort_25 = Product.objects.filter(available=True)[:25]
    sort_50 = Product.objects.filter(available=True)[:50]
    sort_100 = Product.objects.filter(available=True)[:100]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products, 'cart_product_form': cart_product_form})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'recommended_products':recommended_products, 'sort_10':sort_10, 'sort_25':sort_25, 'sort_50':sort_50, 'sort_100':sort_100})

