from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def photo_details(request, pk):
    return render(request, 'photo_details.html')


def profile_details(request):
    return render(request, 'profile_details.html')
