from django.urls import path, register_converter
from . import views as views_geometry, converters

register_converter(converters.UpperConvertor, 'lower_str')


urlpatterns = [
    path('figure/<str:figure>', views_geometry.study_figure),
    path('rectangle/<int:width>/<int:height>', views_geometry.get_rectangle_area, name='rectangle'),
    path('rectangle/<lower_str:value>/', views_geometry.get_conv),
    path('square/<int:width>', views_geometry.get_square_area, name='square'),
    path('circle/<int:radius>', views_geometry.get_circle_area, name='circle'),
    path('get_rectangle_area/<int:width>/<int:height>', views_geometry.rectangle),
    path('get_square_area/<int:width>', views_geometry.square),
    path('get_circle_area/<int:radius>', views_geometry.circle)
]
