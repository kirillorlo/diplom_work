from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Product, Order
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseNotFound
# Create your views here.


# представление главной страницы сайта
def home(request):
    return render(request, 'home.html')


# представление страницы "О нас"
def about(request):
    return render(request, 'about.html')


# представление для регистрации пользователя
def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']

        new_client = Client(name=name, email=email, phone_number=phone_number,
                            address=address)
        new_client.save()
        return HttpResponse('Форма успешно отправлена!')
    return render(request, 'registration.html')


# представления для вхлда пользователя в систему
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        client = Client.objects.filter(name=name, phone_number=phone_number).first()
        if client:
            return redirect('profile')
        else:
            messages.error(request, 'Клиент не найден')
    return render(request, 'home.html')


# представление для обработки информации о продукте
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


# представление для отображения списка продуктов
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_products.html', {'products': products})


# представление для отображения заказа клиента
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    products = order.products.all()

    context = {
        'order': order,
        'client': order.client,
        'products': products,
        'total_amount': order.total_amount,
    }

    return render(request, 'order_detail.html', context)


# представление для создания заказа
def create_order(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            client = Client.objects.get(email=email)
        except Client.DoesNotExist:
            return HttpResponseNotFound('Такого пользователя не существует')
        product_ids = request.POST.getlist('products')
        products = Product.objects.filter(id__in=product_ids)
        order = Order.objects.create(
            client=client,
            total_amount=sum(product.price for product in products)
        )
        order.products.set(products)
        return redirect('order_detail', order_id=order.id)
    else:
        products = Product.objects.all()
        return render(request, 'create_order.html', {'products': products})
