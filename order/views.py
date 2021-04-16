from django.shortcuts import redirect, render
from .models import Order
from product.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def order_checkout_view(request):
    qs = Product.objects.filter(featured=True)
    if not qs.exists():
        return redirect("/")
    product =qs.first()
    user = request.user
    Order.objects.create(product=product, user= user)
    return render(request, 'product/forms.html',{})