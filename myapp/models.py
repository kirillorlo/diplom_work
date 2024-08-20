from django.db import models
# Create your models here.


# модель клиента(пользователя)
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    password = models.BinaryField()
    registration_date = models.DateField(auto_now_add=True)

    def str(self):
        return self.name


# модель продукта
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name


# модель заказа клиента
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Order {self.id} by {self.client.name}"
