from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('posts/', views.main_posts),
    path('posts/<int:number_post>/', views.get_info_about_post_number),
    path('posts/<int:number_post>', views.get_info_about_post_number),
    path('posts/<name_post>/', views.get_info_about_post),
    path('posts/<name_post>', views.get_info_about_post),
]
