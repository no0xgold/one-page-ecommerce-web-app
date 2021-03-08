from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import product
# Create your views here.
def home_view(request):
    return HttpResponse("<h1>welcom</h1>")

def show_detail(request, id):
    try:
        obj = product.objects.get(id=id)
    except product.DoesNotExist:
        raise Http404
    return HttpResponse(f"product id{obj.id}")
    
def api_show_detail(request, id, *args, **kwargs):
    try:
        obj = product.objects.get(id=id)
    except product.DoesNotExist:
        return JsonResponse({"message": "NOT FOUND"},
         status=404)
    return JsonResponse({"id": obj.id})
    