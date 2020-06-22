from django.urls import path

from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('results', views.results, name='results'),
    path('fixtures', views.fixtures, name='fixtures')
]