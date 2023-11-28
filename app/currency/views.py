from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render



def hello(request):
    return HttpResponse('HeloWord!!!')


def tests_templates(request):
    name = request.GET.get('name')
    context = {
        'username': name
    }

    return render(request, 'test.html', context)
