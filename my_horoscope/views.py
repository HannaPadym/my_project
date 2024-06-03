import datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}
zodiac_dates = {
    1: {'capricorn': (1, 20), 'aquarius': (21, 31)},
    2: {'aquarius': (1, 19), 'pisces': (20, 29)},
    3: {'pisces': (1, 20), 'aries': (21, 31)},
    4: {'aries': (1, 20), 'taurus': (21, 30)},
    5: {'taurus': (1, 21), 'gemini': (22, 31)},
    6: {'gemini': (1, 21), 'cancer': (22, 30)},
    7: {'cancer': (1, 22), 'leo': (23, 31)},
    8: {'leo': (1, 21), 'virgo': (22, 31)},
    9: {'virgo': (1, 22), 'libra': (23, 30)},
    10: {'libra': (1, 23), 'scorpio': (24, 31)},
    11: {'scorpio': (1, 22), 'sagittarius': (23, 30)},
    12: {'sagittarius': (1, 22), 'capricorn': (23, 31)}
}


# Create your views here.
def get_my_conv(request, sign_zodiac):
    return HttpResponse(f'Вы передали конвертер - {sign_zodiac}')


def get_main_paige(request):
    zodiacs = list(signs)
    context = {
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_zodiac(request, sign_zodiac):
    if sign_zodiac in signs:
        description = signs.get(sign_zodiac)
        data = {
            'description': description,
            'sign': sign_zodiac.title()
        }
        response = render(request, 'horoscope/info_zodiac.html', context=data)
        return HttpResponse(response)
    return HttpResponseNotFound(f'Не найден такой знак зодиака - {sign_zodiac}')


def get_info_about_zodiac_in_numbers(request, sign_zodiac):
    lst_zodiacs = list(signs)
    if 1 <= sign_zodiac < 12:
        name_zodiac = lst_zodiacs[sign_zodiac - 1]
        redirected_url = reverse('horoscope-name', args=(name_zodiac,))
        return HttpResponseRedirect(redirected_url)
    return HttpResponseNotFound(f'Неправильный порядковый номер - {sign_zodiac}')


def get_info_about_elements(request):
    lst_elements = list(zodiac_element)
    li_elements = ''
    for i in lst_elements:
        li_elements += f'<li><a href="{i}">{i.title()}</a></li>'
    response = f'''
    <ul>
    {li_elements}
    </ul>
'''
    return HttpResponse(response)


def get_info_about_el(request, element):
    li_elements = ''
    type_element = zodiac_element[element]
    for i in type_element:
        redirect_url = reverse('horoscope-name', args=[i])
        li_elements += f'<li><a href="{redirect_url}">{i.title()}</a></li>'
    response = f'''
    <ul>
    {li_elements}
    </ul>
'''
    return HttpResponse(response)


def get_info_about_date(request, month, day):
    try:
        valid_date = datetime.date(2020, month, day)
        print(valid_date)
        sign = ''
        for k, v in zodiac_dates[month].items():
            if day in range(v[0], v[1] + 1):
                sign = k
        redirected_url = reverse('horoscope-name', args=[sign])
        return HttpResponseRedirect(redirected_url)
    except Exception:
        return HttpResponseNotFound('Неправильный формат даты')
