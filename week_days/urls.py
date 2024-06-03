from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('sample_study/', views.get_info_sample),
    path('sample3_study/', views.get_info_sample),
    path('sample2_study/', views.get_guinness_world_records),
    path('people/', views.get_info_about_fake_people),
    path('people2/', views.get_info_about_fake_people2),
    path('<int:day_number>/', views.get_info_about_day_number),
    path('<day_name>/', views.get_info_about_week_day, name='todo_week_name')
]
