from django.conf.urls import url, include

from . import views

urlpatterns = [
    # path('', views.landing, name='landing'),
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),

]