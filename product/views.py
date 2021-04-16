from django.http import request
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from .models import Product
from .forms import productsForm
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.




def search_view(request):
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=query[0])
    print(query ,qs)
    context = {"name": "aux", "query":query}
    return render(request, "home.html", context)
@staff_member_required
def product_create_view(request, *args, **kwargs):
    form = productsForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = productsForm()
    return render(request, "product/forms.html", {"form": form})

def show_detail(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    return render(request, "product/detail.html", {"object": obj})
    
def api_show_detail(request, id, *args, **kwargs):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "NOT FOUND"},
         status=404)
    return JsonResponse({"id": obj.id})
    

def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    #qs: querry set is a list of individual item in model
    context = {"object_list":qs}
    return render(request, "product/list.html", context)