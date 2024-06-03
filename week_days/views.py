from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

dct = {
    'monday': 'в понедельник я жалею себя',
    'tuesday': 'во вторник - глазею в пропасть',
    'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
    'thursday ': 'в четверг - зарядка',
    'friday ': 'ужин с собой, нельзя снова его пропускать',
    'saturday ': 'в субботу - борьба с презрением к себе',
    'sunday ': 'в воскресенье - иду на рождество'
}


# Create your views here.
def index(request):
    return HttpResponse(render(request, "week_days/greeting.html"))


def get_info_about_week_day(request, day_name):
    if day_name in dct:
        return HttpResponse(dct[day_name])
    else:
        return HttpResponseNotFound(f'Нет такого дня недели - {day_name}')


def get_info_about_day_number(request, day_number: int):
    if 1 <= day_number <= 7:
        lst_days = list(dct)
        day = lst_days[day_number - 1]
        redirected_url = reverse('todo_week_name', args=(day,))
        return HttpResponseRedirect(redirected_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {day_number}')


def get_info_sample(request):
    data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны'
    }
    return HttpResponse(render(request, 'week_days/sample.html', context=data))


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'week_days/sample_2.html', context=context)


def get_info_about_fake_people(request):
    people = [
        'Жукова Анна Константиновна',
        'Юлия Степановна Потапова',
        'Гущин Аполлинарий Тимурович',
        'Дорофей Ярославович Третьяков',
        'Селезнева Анна Тарасовна',
        'Федотов Симон Харлампьевич',
        'Красильникова Вера Борисовна',
        'Бажен Тихонович Костин',
        'Веселова Анжелика Тимофеевна',
        'Щербаков Самсон Феодосьевич'
    ]
    data = {
        'people': people
    }
    return render(request, 'week_days/fake_people.html', context=data)


def get_info_about_fake_people2(request):
    people = [
        {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
        {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
        {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
        {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
        {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
        {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
        {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
        {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
        {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
        {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
    ]
    data = {
        'people': people
    }
    return render(request, 'week_days/people_2.html', context=data)
