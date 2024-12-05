from django.shortcuts import render
from .models import Product

def home(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !=" " and item_name is not None:
        product_object= Product.objects.filter(titre__icontains=item_name)
    return render(request, 'shop/index.html',{'product':product_object})

def details(request):
    return render (request,'shop/details.html')
    
    
    # Create your views here.
