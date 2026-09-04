from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        return render(request, 'login.html')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            return render(request, 'dashboard.html', {
                'username': user.username
            })

        return render(request, 'login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'login.html')


def content(request):
    return render(request, 'content.html')


def tasks(request):
    if request.method == 'POST':
        return render(request, 'tasks.html', {
            'message': 'Task submitted successfully!'
        })

    return render(request, 'tasks.html')


def certificate(request):
    username = request.user.username if request.user.is_authenticated else 'Student'

    return render(request, 'certificate.html', {
        'username': username
    })