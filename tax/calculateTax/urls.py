from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),

   
    path("taxrate",views.taxr,name='tax')
    # , path("<str:n>",views.number,name='total')
    ,path("<str:n>",views.number,name='total')



]