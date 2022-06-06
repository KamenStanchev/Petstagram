from django.shortcuts import render


def add_pet(request):
    return render(request, 'pet_create.html')


def pet_edit(request):
    return render(request, 'pet_edit.html')


def pet_delete(request):
    return render(request, 'pet_delete.html')