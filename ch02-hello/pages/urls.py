from django.urls import path  # noqa: D100

from .views import home_page_view

urlpatterns = [
    path("", home_page_view, name="home"),
]
