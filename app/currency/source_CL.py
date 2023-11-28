from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from app.currency.forms import SourceForm
from app.currency.models import Source


class Sourse_of_inform():
    def source_list(request):
        bank = Source.objects.all()
        context = {
            'bank': bank
        }

        return render(request, 'source_list.html', context)

    def source_create(request):  # добавление данных в лист методом ПОСТ
        if request.method == 'POST':  # если метод добавления ПОСТ, от пользователя идут данные то:
            form = SourceForm(data=request.POST)  # Используя метод RateForm получаем request.POST данные.
            if form.is_valid():  # Проверка на правильность и полноту заполнение формы
                form.save()  # Запись данных в базу данных
                return HttpResponseRedirect('/source/list/')  # После переходим на список .
        else:  # Если данные не передаются, то по умолчанию используется метод GET.
            form = SourceForm()  # Форма без заполнения.
        context = {
            'form': form
        }
        return render(request, 'source_create.html', context)
