from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect

from userapp.models import Order
from .models import Book, Genres, UserProfile
from .forms import BookForm, GenreForm


# Create your views here.

def createBook(req):
    if req.method == 'POST':
        form = BookForm(req.POST, files=req.FILES)
        print(form)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form = BookForm()

    genres = Genres.objects.all()

    return render(req, 'admin/createBook.html', {'form': form, 'genres': genres})


def createGenre(req):
    if req.method == 'POST':
        form = GenreForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect('/root/create/')

    else:
        form = GenreForm()
    return render(req, 'admin/genreBook.html', {'form': form})


def adminListBooks(req):
    books = Book.objects.all().order_by('id')

    paginator = Paginator(books, 5)
    pageNumber = req.GET.get('page')

    try:
        page = paginator.get_page(pageNumber)
    except EmptyPage:
        page = paginator.page(pageNumber.num_pages)

    return render(req, 'admin/listbook.html', {'books': books, 'page': page})


def detailBook(req, book_id):
    book = Book.objects.get(id=book_id)
    return render(req, 'admin/detailBook.html', {'book': book})


def editBook(req, book_id):
    book = Book.objects.get(id=book_id)
    genres = Genres.objects.all()

    if req.method == 'POST':
        form = BookForm(req.POST, files=req.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/admin/list/')
        else:
            print(form.errors)

    else:
        form = BookForm(instance=book)

    return render(req, 'admin/updateBook.html', {'form': form, 'genres': genres})


def deleteBook(req, book_id):
    book = Book.objects.get(id=book_id)
    if req.method == 'POST':
        book.delete()
        return redirect('/admin/list/')
    return render(req, 'admin/deleteBook.html', {'book': book})

def searchAdminBook(req):
    query = None
    books = None

    if 'q' in req.GET:
        query = req.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(genre__genre__icontains=query))

    else:
        books = []

    print(req.path)

    context = {'books': books, 'query': query}

    return render(req, 'admin/search.html', context)

def all_users_view(req):
    users = UserProfile.objects.all()
    context = {'users': users}
    return render(req, 'admin/all_users.html', context)

def all_orders_view(req):
    orders = Order.objects.all().select_related('user')
    context = {'orders': orders}
    return render(req, 'admin/all_orders.html', context)

# def register_user(req):
#     if req.method == 'POST':
#         username = req.POST.get('username')
#         email = req.POST.get('email')
#         password = req.POST.get('password')
#         cpassword = req.POST.get('cpassword')
#
#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(req, "This username is already taken")
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(req, "This email id is already registered")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()
#                 return redirect('login')
#         else:
#             messages.info(req, "Password not matching")
#             return redirect('register')
#
#     context = {
#         'background_image': '/static/assets/img/Register.jpg',
#     }
#     return render(req, 'register.html', context)
#
# def login_user(req):
#     if req.method == 'POST':
#         username = req.POST.get('username')
#         password = req.POST.get('password')
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None:
#             if user.username == 'admin':
#                 auth.login(req, user)
#                 return redirect('adminlist')
#             else:
#                 auth.login(req, user)
#                 return redirect('/')
#         else:
#             messages.info(req, "Details entered are not matching")
#             return redirect('login')
#
#     context = {
#         'background_image': '/static/assets/img/Login.jpg',
#     }
#     return render(req, 'login.html', context)
#
# def logout_user(req):
#     auth.logout(req)
#     return redirect('login')

