from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal


class CURRENCY(models.TextChoices):
    EUR = "eur", "EURO"
    USD = "usd", "USD"


class Item(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Item name'
    )
    description = models.CharField(
        max_length=256,
        verbose_name='Item description'
    )
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.5)]
    )
    currency = models.CharField(
        verbose_name='Currency',
        choices=CURRENCY.choices,
        default=CURRENCY.EUR,
        max_length=12
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'


class Discount(models.Model):
    name = models.CharField(
        verbose_name='Name of discount',
        max_length=256,
    )
    amount = models.DecimalField(
        verbose_name='amount',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.0)],
        default=0,
    )

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(
        verbose_name='Tax name',
        max_length=256,
    )
    percent = models.DecimalField(
        verbose_name='amount',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.0)],
        default=0,
    )

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(
        Item,
        verbose_name='Item list',
    )
    currency = models.CharField(
        verbose_name='Currency',
        choices=CURRENCY.choices,
        default=CURRENCY.EUR,
        max_length=12
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Discount',
    )
    tax = models.ForeignKey(
        Tax,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Tax',
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        default_related_name = 'Orders'

    def __str__(self):
        return str(f'order № {self.id}')

    @property
    def price(self):
        total_price = Decimal(0)
        for item in self.items.all():
            total_price += item.price
        if self.discount is not None:
            discount = self.discount.amount
            total_price *= (100 - discount) / 100
        if self.tax is not None:
            tax = self.tax.percent
            total_price += total_price * tax / 100
        return round(total_price, 2)
