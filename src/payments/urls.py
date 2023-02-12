from django.urls import path

from . import views

urlpatterns = [
    path('item/<int:item_id>/', views.main),
    path('buy/<int:item_id>/', views.buy_item, name='buy'),
    path('order/<int:order_id>/', views.order_index, name='order'),
    path('buy-order/<int:order_id>/', views.buy_order, name='order-buy'),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
]
