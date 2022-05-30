from django.urls import path

from Petstagram.main_app.views import home_page

urlpatterns = [
    path('', home_page, name='home_page'),
]