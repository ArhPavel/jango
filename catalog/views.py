from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'all_categories': categories,
    }
    return render(request, 'category_list.html', context)


def category_products(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.products.all()
    context = {
        'category': category,
        'products': products,
        'all_categories': Category.objects.all(),
    }
    return render(request, 'Product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'all_categories': Category.objects.all(),
    }
    return render(request, 'product_detail.html', context)