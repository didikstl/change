from django.contrib import admin
from django.urls import path
from app.currency.views import (
    hello,
    tests_templates

)
from app.currency.rate_CL import Rates
from app.currency.contactUs_CL import Contacts
from app.currency.source_CL import Sourse_of_inform



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/word', hello),
    path('rate/list/', Rates.rate_list),
    path('rate/create/', Rates.rate_create),
    path('rate/update/<int:pk>/', Rates.rate_update),
    path('rate/delete/<int:pk>/', Rates.rate_delete),
    path('rate/details/<int:pk>/', Rates.rate_details),
    path('message/list/', Contacts.message_list),
    path('message/create/', Contacts.message_create),
    path('message/update/<int:pk>/', Contacts.message_update),
    path('message/delete/<int:pk>/', Contacts.message_delete),
    path('message/details/<int:pk>/', Contacts.message_details),
    path('source/list/', Sourse_of_inform.source_list),
    path('source/create/', Sourse_of_inform.source_create),
    path('template/', tests_templates),
]
