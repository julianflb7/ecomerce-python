from django.shortcuts import render
from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

class ProductListView(ListView):
    """docstring for ProductListView."""
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context ['message_1'] = 'Listado de productos'

        return context

class ProductDetailView(DetailView): #La clase DeatilView obtendra un registro de nuestra BD por ID
    model = Product
    template_name = 'products/product.html'

class ProductSearchListView(ListView):
    """docstring for ProductSearchListView."""
    template_name = 'products/search.html'

    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context ['query'] = self.query()
        context['count'] = context['product_list'].count()

        return context
