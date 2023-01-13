from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('home', views.home, name='homepage'),
    path('whoweare/', views.who_we_are, name='whoweare'),
    path('programs/', views.programs, name='programs'),
    path('makeanimpact/', views.make_an_impact, name='impact'),
    path('getintouch/', views.get_in_touch, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('contactform/', views.contact_form, name='contact_form'),
    path("success/", views.success, name="success"),

]