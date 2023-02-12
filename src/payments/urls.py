from django.urls import path

from . import views

urlpatterns = [
    path('item/<int:item_id>/', views.main),
    path('buy/<int:item_id>/', views.buy_item, name='buy'),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
]
