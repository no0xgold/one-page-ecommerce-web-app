"""dj_bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from users.views import register_view, login_view, logout_view
from order.views import (order_checkout_view,Download_Order,
)
from product.views import (search_view,
 show_detail,
 api_show_detail,
 product_create_view,
 product_list_view,)
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='base.html') ),
    path('checkout/', order_checkout_view),
    path('download/', Download_Order),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('search/', search_view),
    path('products/create/', product_create_view),#anoher option is products-create
    path('products/<int:id>', show_detail),
    path('products/', product_list_view),
    #path('api/products/<int:id>',  api_show_detail),
    re_path(r'api/products/(?P<id>\d+)/', api_show_detail),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)