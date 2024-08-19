from django.urls import path
from . import views

urlpatterns = [
    path('', views.listBooks, name='list'),
    path('detailbook/<int:book_id>/', views.detailBook, name='bookdetails'),
    path('searchpage/', views.searchBook, name='searchpage'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='addtocart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove_cart/<int:item_id>/', views.remove_from_cart, name='remove_cart'),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('contact_us/', views.contact, name='contact'),
    path('order-history/', views.order_history, name='order-history'),   
]