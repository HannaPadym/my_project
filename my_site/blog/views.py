from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
facts = {'fact_1': 'Самая крупная жемчужина в мире достигает 6 килограммов в весе.',
         'fact_2': 'Законодательство США допускало отправку детей по почте до 1913 года.',
         'fact_3': 'В языке древних греков не существовало слова, которое обозначало религию.',
         'fact_4': 'В современной истории есть промежуток времени, когда на счетах компании «Apple», было больше средств, чем у американского правительства.',
         'fact_5': 'Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.',
         'fact_6': 'В Ирландии никогда не было кротов.',
         'fact_7': 'Флот США содержит больше авианосцев, чем все флоты мира вместе взятые.',
         'fact_8': 'Скорость распространения лавы после извержения, близка к скорости бега гончей.',
         'fact_9': 'Изначально, отвертка была изобретена для выковыривания гвоздей, шуруп был изобретен на 100 лет позже.',
         'fact_10': 'Библия – книга, которую чаще всего воруют в американских магазинах.'}


def main_page(request):
    return HttpResponse(render(request, 'blog/index.html'))


def main_posts(request):
    return HttpResponse(render(request, 'blog/list_detail.html'))


def get_info_about_post(request, name_post):
    data = {
        name_post: 'name_post'
    }
    return HttpResponse(render(request, 'blog/detail_by_name.html', context=data))


def get_info_about_post_number(request, number_post):
    data = {
       'number_post': number_post
    }
    return HttpResponse(render(request, 'blog/detail_by_number.html', context=data))
