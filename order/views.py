import pathlib
from django import forms
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from mimetypes import guess_type
from .models import Order
from .forms import OrderForm
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.http import Http404
from wsgiref.util import FileWrapper
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

@login_required
def Download_Order(request, *args, **kwargs):
    qs =Product.objects.filter(media__isnull=False)
    product_obj= qs.first()
    if not product_obj.media:
        raise Http404
    media = product_obj.media
    product_path = media.path
    path = pathlib.Path(product_path)
    pk = product_obj.id
    extinction =path.suffix #.png
    filename=f'{pk}{extinction}'
    if not path.exists():
        raise Http404
    with open(path,'rb') as f:
        wrapper =FileWrapper(f)
        content_type= 'application/force_download'
        guessed_ = guess_type(path)[0]
        if guessed_:
            content_type = guessed_
        response = HttpResponse(wrapper, content_type=content_type)
        response['Content-Disposition'] = f'attachment;filename={filename}'
        response['X-SendFile'] = f'{filename}'
        return response