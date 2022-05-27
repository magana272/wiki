from django.urls import path

from . import views

urlpatterns = [
    path("", views.to_index, name="to_index"),
    path("wiki/", views.index, name="index"),
    path("wiki/<str:page>", views.page, name = "page")
]
