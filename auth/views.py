from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login, logout

def Login(request):
    Username = request.POST.get('username')
    Password = request.POST.get('password')

    error = ""

    user = authenticate(request, username = Username, password = Password)

    if user is not None:
        login(request , user)
        # Redirect to success page
        return render(request, 'home/index.html')

    else:
        error = "Invalid UserName or Password"
        return render(request, 'auth/login.html', {'error' : error})


def Logout(request):
    logout(request)
    return render(request, 'home/index.html')