from django.shortcuts import render, redirect

from Petstagram.main_app.models import PetPhoto


def add_photo(request):
    return render(request, 'photo_create.html')


def photo_edit(request):
    return render(request, 'photo_edit.html')


def photo_details(request, pk):
    pet_photo = PetPhoto.objects.get(id=pk)
    contex = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', contex)


def like_photo(request, pk):
    pet_photo = PetPhoto.objects.get(id=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo_details', pk)