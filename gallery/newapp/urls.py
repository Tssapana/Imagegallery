from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('upload/', views.upload_image, name='upload_form'),
    path('login/',views.login_user, name='login'),
    path('logout', views.logout_user, name="logout")
]