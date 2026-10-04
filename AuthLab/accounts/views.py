from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(req):
    if req.method == 'POST':
        print(User)
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')

#1. set_password()

# Password ko hash karke user ke password field mein set karta hai.

# Conceptually:

# user.set_password("Pranjal@123")

# Iske baad:

# user.password

# mein plain password nahi, hashed representation hoti hai.


# '''2. check_password()

# Login ke waqt entered password ko stored hash ke against verify karta hai.

# Conceptually:

# user.check_password("Pranjal@123")

# Result:

# True

# ya

# False'''

        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            print(f"User created: {user.username}")
        else:
            print("Passwords do not match")
    return render(req, 'accounts/register.html')



def login_view(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # Django's built-in authentication system provides a convenient way to authenticate users. You can use the `authenticate` function to verify the username and password.
        user = authenticate(
             username = username,
             password = password
        )  
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else :
            print("Invalid Credentials")

    return render(request, "accounts/login.html")

@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")


