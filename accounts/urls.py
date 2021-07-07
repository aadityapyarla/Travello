from . import views
from django.urls.conf import include, path 
import debug_toolbar

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('__debug__/', include(debug_toolbar.urls), name='logout'),

]

