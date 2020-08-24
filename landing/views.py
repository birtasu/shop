from django.shortcuts import render
from .forms import SubscriberForm

from products.models import ProductImage


# Create your views here.
def landing(request):
    name = 'admin'
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        # email = form.cleaned_data['email']
        # print(email)
        form_save = form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
    products = ProductImage.objects.filter(is_active=True, product__is_active=True)
    return render(request, 'landing/home.html', locals())