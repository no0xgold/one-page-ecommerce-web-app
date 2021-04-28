from django import forms
from django.shortcuts import redirect, render
from .models import Order
from .forms import OrderForm
from product.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def order_checkout_view(request):
    qs = Product.objects.filter(featured=True)
    if not qs.exists():
        return redirect("/")
    product =qs.first()
    #if not product.has_inventory:
        #return redirect("/no inventory")
    user = request.user
    order_id= request.session.get("order_id")
    order_obj = None
    new_creation = False
    try:
        order_obj = Order.objects.get(id=order_id)
    except:
        order_id=None
    if order_id == None and order_obj==None:
        new_creation = True
        order_obj=Order.objects.create(product=product, user= user)
        request.session['order_id']=order_obj.id
    print(order_obj.id)
    if order_obj != None:
        if order_obj.product.id != product.id:
            order_obj=Order.objects.create(product=product, user= user)
    request.session['order_id']=order_obj.id
    form = OrderForm(request.POST or None ,product=product, instance=order_obj)
    if form.is_valid():
        order_obj.shipping_address = form.cleaned_data.get("shipping_address")
        order_obj.building_address = form.cleaned_data.get("building_address")
        order_obj.mark_paid(save=False)
        order_obj.save()
        del request.session['order_id']
        return redirect("/success")
    return render(request, 'order/checkout.html',{"form":form,'object':order_obj})