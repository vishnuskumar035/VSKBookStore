from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Create your models here.

class Genres(models.Model):
    genre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '{}'.format(self.genre)


class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    dPrice = models.IntegerField(null=True)
    dPercent = models.IntegerField(null=True)
    pages = models.IntegerField(null=True)
    language = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='book_media', null=True)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)
    summary = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return '{}'.format(self.title)
    
class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True, null=True)
    email = models.EmailField(max_length=200, unique=True, null=True)
    password = models.CharField(max_length=200, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

# class LoginTable(models.Model):
#     username = models.CharField(max_length=200, null=True)
#     email = models.EmailField(max_length=200, null=True)
#     password = models.CharField(max_length=200, null=True)
#     cpassword = models.CharField(max_length=200, null=True)
#     type = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return '{}'.format(self.username)