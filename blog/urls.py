from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home.html'),
    path('add_product/', views.add_product, name='add_product'),
    path('view_inventory/', views.view_inventory, name='view_inventory'),
    path('record_sale/', views.record_sale, name='record_sale'),
    path('add_customerID/', views.add_customerID, name='add_customerID'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)