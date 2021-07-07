from . import views
from django.urls.conf import path 


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('contact', views.contact, name='contact'),
    path('destinations', views.destinations, name='destinations')

]

