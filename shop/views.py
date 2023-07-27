from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Products, Cart, Address
from django.shortcuts import redirect, get_object_or_404

# Create your views here.

# @login_required
def home(request):
    products = Products.objects.all()

    cart_items = Cart.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'home.html', {'products': products, 'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')


def remove_from_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    cart_item = get_object_or_404(Cart, user=request.user, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('home')

def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin_code = request.POST.get('pin')

        address = Address(user=request.user, address=address, city=city, state=state, pin_code=pin_code)
        address.save()


        return redirect('home')

    return redirect('home')