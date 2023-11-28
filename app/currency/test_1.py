# _______________________old_URLS_________________________________

# from django.contrib import admin
# from django.urls import path
# from app.currency.views import (
#     hello,
#     message,
#     tests_templates,
#     # rate_list,
#     # rate_create,
#     # rate_update,
#     # rate_delete,
#
# )
# from app.currency.rate_CL import Rates
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('hello/word', hello),
#     path('rate/list/', Rates.rate_list),
#     path('rate/create/', Rates.rate_create),
#     path('rate/update/<int:pk>/', Rates.rate_update),
#     path('rate/delete/<int:pk>/', Rates.rate_delete),
#     path('contactus/list', message),
#     path('template/', tests_templates),
# ]




# ______________________________ld_views_______________________

# Rates.rate_list()
#
# Rates.rate_create()
#
# Rates.rate_update()
#
# Rates.rate_delete()

# def rate_list(request): # Список рейтов
#     rates = Rate.objects.all()
#     context = {
#         'rates': rates
#     }
#
#     return render(request, 'rate_list.html', context)
#
#
# def rate_create(request):  # добавление данных в рейт_лист методом ПОСТ
#     if request.method == 'POST': # если метод добавления ПОСТ, от пользователя идут данные то:
#         form = RateForm(data=request.POST) # Используя метод RateForm получаем request.POST данные.
#         if form.is_valid(): # Проверка на правильность и полноту заполнение формы
#             form.save() # Запись данных в базу данных
#             return HttpResponseRedirect('/rate/list/') # После переходим на список рейтов.
#     else: # Если данные не передаются, то по умолчанию используется метод GET.
#         form = RateForm() # Форма без заполнения.
#     context = {
#         'form': form
#     }
#     return render(request, 'rate_create.html', context)
#
#
# def rate_update(request, pk): # Изменения данных в рейтах по ID.
#     rate = Rate.objects.get(id=pk) # Через модель Rate по ID (pk-primary key)
#
#     if request.method == 'POST':
#         form = RateForm(request.POST, instance=rate)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list/')
#     elif request.method == 'GET':
#         form = RateForm(instance=rate)
#     context = {
#         'form': form
#     }
#     return render(request, 'rate_update.html', context)
#
#
# def rate_delete(request, pk): # Удаление данных из базы рейтов по ID.
#     rate = Rate.objects.get(id=pk)
#
#     if request.method == 'GET':
#         context = {
#             'rate': rate
#         }
#         return render(request, 'rate_delete.html', context)
#
#
#     elif request.method == 'POST':
#         rate.delete()
#         return HttpResponseRedirect('/rate/list/')



# def message(request):
#     infos = ContactUs.objects.all()
#     context = {
#         'infos': infos
#     }
#
#     return render(request, 'message_list.html', context)