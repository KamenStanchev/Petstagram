from django.shortcuts import render, redirect

from Petstagram.main_app.models import Profile, PetPhoto


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
    # profile = get_profile()
    # pets = profile.pet_set.all()
    pet_photos = PetPhoto.objects.all()
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)


def photo_details(request, pk):
    pet_photo = PetPhoto.objects.get(id=pk)
    contex = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', contex)


def profile_details(request):
    profile = get_profile()

    profile_images = (PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct())
    total_images = len(profile_images)
    total_likes = sum(p_pic.likes for p_pic in profile_images)
    context = {
        'profile': profile,
        'total_images': total_images,
        'total_likes': total_likes,
    }
    return render(request, 'profile_details.html', context)


def unauthorized(request):
    return render(request, '401_error.html')


def like_photo(request, pk):
    pet_photo = PetPhoto.objects.get(id=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo_details', pk)
