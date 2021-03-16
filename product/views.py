from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import product
from .forms import productsForm
# Create your views here.




def search_view(request):
    query = request.GET.get('q')
    qs = product.objects.filter(title__icontains=query[0])
    print(query ,qs)
    context = {"name": "aux", "query":query}
    return render(request, "home.html", context)

def product_create_view(request, *args, **kwargs):
    #print(request.POST)
    #print(request.GET)
    if request.method == "POST":
        post_data = request.POST or None#another option is empty dictionary
        if post_data != None:
            my_form  = productsForm(request.POST)
            if my_form.is_valid():
                print(my_form.cleaned_data.get("title"))#it should be match to the name of form class that we use in this view 
                title_form_input = my_form.cleaned_data.get("title")
                product.objects.create(title=title_form_input)
    return render(request, "product/forms.html", {})

def show_detail(request, id):
    try:
        obj = product.objects.get(id=id)
    except product.DoesNotExist:
        raise Http404
    return render(request, "product/detail.html", {"object": obj})
    
def api_show_detail(request, id, *args, **kwargs):
    try:
        obj = product.objects.get(id=id)
    except product.DoesNotExist:
        return JsonResponse({"message": "NOT FOUND"},
         status=404)
    return JsonResponse({"id": obj.id})
    

def product_list_view(request, *args, **kwargs):
    qs = product.objects.all()
    #qs: querry set is a list of individual item in model
    context = {"object_list":qs}
    return render(request, "product/list.html", context)