# from django.contrib import messages
# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.shortcuts import redirect

# # Create your views here.
# def register(request):
#     if request.method== 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         cpassword = request.POST['password1']

#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"Username Taken")
#                 return redirect('register')
#             if User.objects.filter(email=email).exists():
#                 messages.info(request,"Email Taken")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name,email=email)
#                 user.save()
                
#         else:
#             messages.info(request,"Verify Password")
#             return redirect('register')
#         return redirect('/')

#     return render(request,"register.html")

from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
            if password != cpassword:
                messages.info(request, "Verify Password")

            if not any(messages.get_messages(request)):
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                # No need to call user.save()

                # Redirect to the home page or another desired page after successful registration
                return redirect('login')

        else:
            messages.info(request, "Verify Password")

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Ivalid Credentials")
    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')