from django.urls import path

from core import views


# from .views import say_hello

urlpatterns = [
    path("something_cool/", views.something_cool, name="something_cool"),
    path("", views.testView, name="home"),
]
