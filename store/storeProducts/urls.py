from django.urls import path, include

from . import views
from .views import basket_add, basket_remove, IndexView, ProductListView

app_name = 'storeProducts'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/category/<int:category_id>/', ProductListView.as_view(), name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
