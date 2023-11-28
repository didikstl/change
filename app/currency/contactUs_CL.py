from app.currency.models import ContactUs
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from app.currency.forms import MessageForm


class Contacts():
    def message_list(request):
        infos = ContactUs.objects.all()
        context = {
            'infos': infos
        }

        return render(request, 'message_list.html', context)

    def message_create(request):  # добавление данных в рейт_лист методом ПОСТ
        if request.method == 'POST':  # если метод добавления ПОСТ, от пользователя идут данные то:
            form = MessageForm(data=request.POST)  # Используя метод RateForm получаем request.POST данные.
            if form.is_valid():  # Проверка на правильность и полноту заполнение формы
                form.save()  # Запись данных в базу данных
                return HttpResponseRedirect('/message/list/')  # После переходим на список рейтов.
        else:  # Если данные не передаются, то по умолчанию используется метод GET.
            form = MessageForm()  # Форма без заполнения.
        context = {
            'form': form
        }
        return render(request, 'message_list_create.html', context)

    def message_update(request, pk):  # Изменения данных в рейтах по ID.
        info_ = ContactUs.objects.get(id=pk)  # Через модель Rate по ID (pk-primary key)

        if request.method == 'POST':
            form = MessageForm(request.POST, instance=info_)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/message/list/')
        elif request.method == 'GET':
            form = MessageForm(instance=info_)
        context = {
            'form': form
        }
        return render(request, 'message_list_update.html', context)

    def message_delete(request, pk):  # Удаление данных из базы рейтов по ID.
        info_ = ContactUs.objects.get(id=pk)

        if request.method == 'GET':
            context = {
                'info_': info_
            }
            return render(request, 'message_list_delete.html', context)


        elif request.method == 'POST':
            info_.delete()
            return HttpResponseRedirect('/message/list/')

    def message_details(request, pk):
        info = ContactUs.objects.get(id=pk)
        context = {
            'info': info
        }
        return render(request, 'message_details.html', context)
