from django.urls import path, register_converter
from . import views as views_horoscope, converters

register_converter(converters.SplitConverter, 'my_conv')


urlpatterns = [

    path('type/', views_horoscope.get_info_about_elements),
    path('<my_conv:sign_zodiac>/', views_horoscope.get_my_conv),
    path('type/<str:element>/', views_horoscope.get_info_about_el, name='type_name'),
    path('', views_horoscope.get_main_paige),
    path('<int:month>/<int:day>/', views_horoscope.get_info_about_date),
    path('<int:sign_zodiac>/', views_horoscope.get_info_about_zodiac_in_numbers),
    path('<str:sign_zodiac>/', views_horoscope.get_info_about_zodiac, name='horoscope-name'),


]
