from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse


# Create your views here.
def study_figure(request, figure: str):
    return HttpResponse(render(request, f'geometry/{figure}.html'))


def get_conv(request, value: str):
    return HttpResponse(f'Вы передали конвертер - {value}')


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'{width * height}')


def get_square_area(request, width: int):
    return HttpResponse(f'{width ** 2}')


def get_circle_area(request, radius: int):
    return HttpResponse(f'{pi * radius ** 2}')


def rectangle(request, width: int, height: int):
    redirected_url = reverse('rectangle', args=[width, height])
    return HttpResponseRedirect(redirected_url)


def square(request, width: int):
    redirected_url = reverse('square', args=(width,))
    return HttpResponseRedirect(redirected_url)


def circle(request, radius: int):
    redirected_url = reverse('circle', args=(radius,))
    return HttpResponseRedirect(redirected_url)
