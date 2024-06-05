import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_add = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class PizzaCategory(BaseModel):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name


class Pizza(BaseModel):
    category = models.ForeignKey(PizzaCategory, on_delete=models.CASCADE, related_name="pizzas")
    pizza_name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    images = models.ImageField(upload_to="core/images")
    def __str__(self):
        return self.pizza_name


class Cart(BaseModel):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="cart")
    is_paid = models.BooleanField(default=False)



class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item")
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, )
