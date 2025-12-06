# path === urls === chrome input
# urls === file === html(views)

from django.urls import path
from .views import home
urlpatterns = [
    path("", home, name="home")
]
