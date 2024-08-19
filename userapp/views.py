from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from bookApp.models import Book
from userapp.models import Cart, CartItem, Order, OrderItem
from django.contrib import messages
from django.conf import settings
import stripe


# Create your views here.

def listBooks(req):
    books = Book.objects.all().order_by('id')

    paginator = Paginator(books, 4)
    pageNumber = req.GET.get('page')

    try:
        page = paginator.get_page(pageNumber)
    except EmptyPage:
        page = paginator.page(pageNumber.num_pages)

    return render(req, 'user/baseBookList.html', {'books': books, 'page': page})

def detailBook(req, book_id):
    book = Book.objects.get(id=book_id)
    return render(req, 'user/bookDetail.html', {'book': book})

def searchBook(req):
    query = None
    books = None

    if 'q' in req.GET:
        query = req.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(genre__genre__icontains=query))

    else:
        books = []

    context = {'books': books, 'query': query}

    return render(req, 'user/searchpage.html', context)

def add_to_cart(req, book_id):
    book = Book.objects.get(id=book_id)

    if book.quantity > 0:
        cart, created = Cart.objects.get_or_create(user=req.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('view_cart')


def view_cart(req):
    # cart, created = Cart.objects.get_or_create(user=req.user)
    user = req.user
    print(user)
    if not user.is_authenticated:
        # Handle the case where the user is not authenticated
        messages.error(req, "You need to log in to view your cart.")
        return redirect('login')
    
    cart, created = Cart.objects.get_or_create(user=req.user)
    cart_items = cart.cartitem_set.all()
    cart_item = CartItem.objects.all()
    total_price = sum(item.book.price * item.quantity for item in cart_items)
    total_discount_price = sum(item.book.dPrice * item.quantity for item in cart_items)
    total_discount = (total_price - total_discount_price)
    total_items = cart_items.count()

    context = {'cart_items': cart_items, 'cart_item': cart_item, 'total_price': total_price, 'total_items': total_items, 'total_discount_price': total_discount_price, 'total_discount': total_discount}

    return render(req, 'user/cart.html', context)

def increase_quantity(req, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity < cart_item.book.quantity:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

def decrease_quantity(req, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('view_cart')

def remove_from_cart(req, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
    except cart_item.DoesNotExist:
        pass

    return redirect('view_cart')

def create_checkout_session(req):
    cart_items = CartItem.objects.all()

    if cart_items:
        stripe.api_key = settings.STRIPE_SECRET_KEY

        if req.method == 'POST':
            line_items = []
            for cart_item in cart_items:
                if cart_item.book:
                    line_item = {
                        'price_data': {
                            'currency': 'INR',
                            'unit_amount': int(cart_item.book.dPrice * 100),
                            'product_data':{
                                'name': cart_item.book.title
                            },
                        },
                        'quantity': 1
                    }

                    line_items.append(line_item)
            
            if line_items:
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types= ['card'],
                    line_items= line_items,
                    mode= 'payment',
                    success_url= req.build_absolute_uri(reverse('success')),
                    cancel_url= req.build_absolute_uri(reverse('cancel')),
                )

                return redirect(checkout_session.url, code = 303)
            
def success(req):
    cart_items = CartItem.objects.all()
    user = req.user

    if cart_items:
        total_amount = sum(item.book.dPrice * item.quantity for item in cart_items)

        order = Order.objects.create(
            user = user,
            total_price = total_amount,
        )

    for cart_item in cart_items:
        product = cart_item.book

        OrderItem.objects.create(
                order=order,
                book=cart_item.book,
                quantity=cart_item.quantity,
                price=cart_item.book.dPrice
            )

        if product.quantity >= cart_item.quantity:
            product.quantity -= cart_item.quantity
            product.save()

    cart_items.delete()

    return render(req, 'user/success.html')

def cancel(req):
    return render(req, 'user/cancel.html')

def order_history(req):
    orders = Order.objects.filter(user=req.user).prefetch_related('items__book')
    context = {'orders': orders}
    return render(req,'user/order_history.html', context)

def contact(req):
    return render(req, 'user/contact.html')