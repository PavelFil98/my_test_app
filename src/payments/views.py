import stripe
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from djangostripe.settings import (STRIPE_PUBLISHABLE_KEY,
                                   STRIPE_SECRET_KEY, YOUR_DOMAIN)
from .models import Item

stripe.api_key = STRIPE_SECRET_KEY


def main(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(
        request,
        'index.html',
        {
            'item': item,
            'STRIPE_PUBLIC_KEY': STRIPE_PUBLISHABLE_KEY
        }
    )


def buy_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount_decimal': item.price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success/',
        cancel_url=YOUR_DOMAIN + '/cancelled/',
    )
    return JsonResponse({'id': session['id']})


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
