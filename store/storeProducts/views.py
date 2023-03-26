from django.shortcuts import render, HttpResponseRedirect

from .models import Product, ProductCategory, Basket
import sys
sys.path.append('/Users/erlankarabaliyev/Desktop/spring kbtu/django/djangoProject/store/users')
from users .models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'storeProducts/index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context

# def index(request):
#     context = {
#         'title' : 'storeApp',
#         # 'categories' : ProductCategory.objects.all(),
#     }
#
#     return render(request, 'storeProducts/index.html', context)
#


class ProductListView(ListView):
    model = Product
    template_name = 'storeProducts/products.html'
    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['title'] = 'storeApp'
        context['categories'] = ProductCategory.objects.all()
        return context


# def products(request, category_id=None):
#     if category_id:
#         category = ProductCategory.objects.get(id = category_id)
#         products = Product.objects.filter(category = category)
#     else:
#         products = Product.objects.all()
#
#     context = {
#         'title' : 'storeApp',
#         'products' : products,
#         'categories' : ProductCategory.objects.all(),
#     }
#     return render(request, 'storeProducts/products.html', context)
#

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])





