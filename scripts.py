import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Lesson, Commendation


def fix_marks(schoolkid):
    count = schoolkid.mark_set.filter(points__in=[2, 3]).update(points=5)
    return count


def remove_chastisements(schoolkid):
    schoolkid.chastisement_set.all().delete()


def create_commendation(name, subject_title):
    try:
        schoolkid = Schoolkid.objects.get(full_name__icontains=name)
    except ObjectDoesNotExist:
        print(f"Ошибка: ученик {name}, не найден")
        return
    except MultipleObjectsReturned:
        print("Ошибка: слишком много людей с таким именем, уточните ФИО")
        return

    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
    ]

    lesson = (Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title__icontains=subject_title).order_by('-date').first())

    Commendation.objects.create(text=random.choice(commendations),
                                created=lesson.date,
                                schoolkid=schoolkid,
                                subject=lesson.subject,
                                teacher=lesson.teacher)
