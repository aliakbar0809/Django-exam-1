from django.urls import path
from .views import *

urlpatterns = [

    path('users/',user_list,name='user_list'),
    path('users/create/',user_create,name='user_create'),
    path('users/<int:id>/',user_detail,name='user_detail'),
    path('users/<int:id>/update/',user_update,name='user_update'),
    path('users/<int:id>/delete/',user_delete,name='user_delete'),


    path('videos/',video_list,name='video_list'),
    path('videos/create/',video_create,name='video_create'),
    path('videos/<int:id>/',video_detail,name='video_detail'),
    path('videos/<int:id>/update/',video_update,name='video_update'),
    path('videos/<int:id>/delete/',video_delete,name='video_delete'),

    path('login/',login,name='login'),
    path('logout/',logout,name='logout')
]