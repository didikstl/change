from django.contrib import admin
from django.urls import path
from app.currency.views import hello, rate_list, message, tets_templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/word', hello),
    path('rate/list', rate_list),
    path('contactus/list', message),
    path('template/', tets_templates),

]
