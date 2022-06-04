from django.urls import path

from Petstagram.main_app.views import home_page, dashboard, profile_details, photo_details, like_photo

urlpatterns = [
    path('', home_page, name='home_page'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile_details, name='profile_details'),
    path('photo/details/<str:pk>/', photo_details, name='photo_details'),
    path('photo/like/<str:pk>/', like_photo, name='like_photo'),
]