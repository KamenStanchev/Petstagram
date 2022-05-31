from django.shortcuts import render

from Petstagram.main_app.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    context = {
        'hide_additional_nav_item': True,
    }
    return render(request, 'home_page.html', context)


def dashboard(request):
    profile = get_profile()
    pets = profile.pet_set.all()
    context = {
        'pets': pets,
    }
    return render(request, 'dashboard.html', context)


def photo_details(request, pk):
    return render(request, 'photo_details.html')


def profile_details(request):
    return render(request, 'profile_details.html')
