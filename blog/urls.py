from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', views.base, name='base'),
    path('base', views.post_list, name='base'),
    path('add_products/', views.add_product, name='add_products'),
    path('view_inventory/', views.inventory, name='view_inventory'),
    path('record_sale/', views.record_sale, name='record_sale'),
    path('customer/', views.customer, name='customer'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)