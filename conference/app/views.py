from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'signin.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'signup.html', {'error': error_message})

    return render(request, 'signup.html')


def signin(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'signin.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'signin.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name})

@login_required
def conferencing(request):
    return render(request, 'conference.html', {'name': request.user.first_name + " " + request.user.last_name})

@login_required
def signout(request):
    logout(request)
    return redirect("/signin")

@login_required
def join(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'join.html')