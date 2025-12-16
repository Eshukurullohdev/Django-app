# path === urls === chrome input
# urls === file === html(views)

from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("second/", second_html, name="second"),
    path("nav/", navigation, name="nav")
]
