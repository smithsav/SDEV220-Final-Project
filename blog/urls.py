from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='base.html'),
    path('add_product/', views.add_product, name='add_product.html'),
    path('view_inventory/', views.view_inventory, name='view_inventory.htmlh'),
    path('record_sale/', views.record_sale, name='record_sale.html'),
    path('add_customerID/', views.add_customerID, name='add_customerID.html'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)