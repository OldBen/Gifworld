#from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('csgo', views.csgo, name='csgo'),
    path('ow', views.ow, name='ow'),
    path('csgo/filter', views.csgo_filter, name='csgo_filter'),
    path('ow/filter', views.ow_filter, name='ow_filter'),
    path('csgo/<int:id>', views.csgo_detail, name='csgo_detail'),
    path('ow/<int:id>', views.ow_detail, name='ow_detail'),
    path('csgo/create', views.csgo_create, name='csgo_create'),
    path('ow/create', views.ow_create, name='ow_create'),
]
