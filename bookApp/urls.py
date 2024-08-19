from django.urls import path
from . import views
from authapp import views as authviews

urlpatterns = [
    path("create/", views.createBook, name='create'),
    path("genre/", views.createGenre, name='genre'),
    path('list/', views.adminListBooks, name='adminlist'),
    path('detailsbook/<int:book_id>', views.detailBook, name='details'),
    path('updatebook/<int:book_id>', views.editBook, name='edit'),
    path('deletebook/<int:book_id>', views.deleteBook, name='delete'),
    path('search/', views.searchAdminBook, name='search'),
    path('', authviews.userLogin, name='loginadmin'),
    path('all_users/', views.all_users_view, name='all_users'),
    path('all_orders/', views.all_orders_view, name='all_orders'),
]