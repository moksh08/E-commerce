from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'myapp/product_detail.html', {'product': product})
from django.shortcuts import render, redirect

def add_product(request):
    if request.method == 'POST':
        prod = Product()
        prod.name = request.POST.get("p_name", False)
        prod.price = request.POST.get("p_price", False)
        prod.description = request.POST.get("p_model", False)
        prod.image = request.FILES.get("p_photo", False)
        prod.save()
        return redirect('/')
    return render(request, 'myapp/add_product.html')
