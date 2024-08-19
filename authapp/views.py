from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from bookApp.forms import UserProfileForm, UserLoginForm
from bookApp.models import UserProfile


# Create your views here.

def userRegistration(req):
    if req.method == 'POST':
        form = UserProfileForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('login')
        
    else:
        form = UserProfileForm()

    context = {'background_image': '/static/assets/img/Register.jpg', 'form': form}
    return render(req, 'auth/register.html', context)


def userLogin(req):
    if req.method == 'POST':
        form = UserLoginForm(req, req.POST)
        print(form.is_valid())
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, email=email, password=password)
            print(user)

            if user is not None:
                login(req, user)
                
                if user.is_superuser:
                    req.session['username'] = user.username
                    return redirect('adminlist')
                else:
                    req.session['username'] = user.username
                    return redirect('list')
            else:
                messages.error(req, 'Invalid credentials')
    else:
        form = UserLoginForm()
    
    context = {'background_image': '/static/assets/img/Login.jpg','form': form}

    return render(req, 'auth/login.html', context)

def userLogout(req):
    logout(req)
    return redirect('login')




# def userRegistration(req):
#     # loginTable = LoginTable()
#     # userProfile = UserProfile()

#     if req.method == 'POST':
#         # userProfile.username = req.POST['username']
#         # userProfile.email = req.POST['email']
#         # userProfile.password = req.POST['password']
#         # userProfile.cpassword = req.POST['cpassword']
#         #
#         # loginTable.username = req.POST['username']
#         # loginTable.email = req.POST['email']
#         # loginTable.password = req.POST['password']
#         # loginTable.cpassword = req.POST['cpassword']
#         # loginTable.type = 'user'
#         username = req.POST['username']
#         email = req.POST['email']
#         password = req.POST['password']
#         cpassword = req.POST['cpassword']

#         if password == cpassword:
#             if UserProfile.objects.filter(email=email).exists():
#                 messages.error(req, "Email already exists")
#             elif UserProfile.objects.filter(username=username).exists():
#                 messages.error(req, "Username already exists")
#             else:
#                 user = UserProfile.objects.create(email=email, username=username, password=password)
#                 user.save()
#                 messages.success(req, "User registered successfully")
#                 # loginTable.save()
#             return redirect('login')
#         else:
#             messages.error(req, 'Password not matching')
#             return redirect('register')

#     context = {'background_image': '/static/assets/img/Register.jpg'}
#     return render(req, 'auth/register.html', context)


# def userLogin(req):
#     # if req.method == 'POST':
#     #     username = req.POST['username']
#     #     password = req.POST['password']
       
#     #     # user = LoginTable.objects.filter(username=username,password=password,type='user').exists()
#     #     # user = authenticate(req, username=username,password=password)
#     #     # print(user)
#     #     try:
#     #         # if user is not None:
#     #             # user_details = LoginTable.objects.get(username=username, password=password)
#     #             # user_name = user_details.username 
#     #             # type=user_details.type
                
                

#     #             # if user.is_admin:
#     #             #     req.session['username'] = user.username
#     #             #     return redirect('adminlist')
#     #             # else:
#     #             #     req.session['username'] = user.username
#     #             #     return redirect('list')

#     #             if type == 'user':
#     #                 req.session['username'] = user_name
#     #                 return redirect('list')
#     #             elif type == 'admin':
#     #                 req.session['username'] = user_name
#     #                 return redirect('adminlist')
#     #         else:
#     #             messages.error(req, "Invalid Credentials")

#     #     except:
#     #         messages.error(req, "Invalid role")
#     # context = {'background_image': '/static/assets/img/Login.jpg'}
#     # return render(req, 'auth/login.html', context)

# # def userLogout(req):
# #     logout(req)
# #     return redirect('login')