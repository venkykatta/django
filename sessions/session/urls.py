from django.urls import path

from . import views

urlpatterns = [
    path('cookie_session', views.cookie_session, name = 'cookie_session'),
    path('cookie_delete', views.cookie_delete, name = 'cookie_delete')
]