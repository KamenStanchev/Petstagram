from django.shortcuts import render, redirect

from Petstagram.main_app.forms import PhotoCreateForm
from Petstagram.main_app.models import PetPhoto
from Petstagram.main_app.views.others import get_profile


def add_photo(request):
    if request.method == 'POST':
        form = PhotoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = PhotoCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'photo_create.html', context)


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