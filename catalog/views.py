from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Product, Category


class ContactsView(TemplateView):
    """Страница контактов (Задание 1)"""
    template_name = 'catalog/contacts.html'


class CategoryListView(ListView):
    """Список всех категорий (на главную страницу)"""
    model = Category
    context_object_name = 'categories'


class ProductListView(ListView):
    """Список товаров (всех или конкретной категории)"""
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_pk = self.kwargs.get('pk')
        if category_pk:
            queryset = queryset.filter(category_id=category_pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_pk = self.kwargs.get('pk')
        if category_pk:
            context['category'] = get_object_or_404(Category, pk=category_pk)
        return context


class ProductDetailView(DetailView):
    """Страница одного товара"""
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    success_url = reverse_lazy('catalog:category_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category_list')
