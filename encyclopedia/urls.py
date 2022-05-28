from django.urls import path

from . import views

urlpatterns = [
    path("", views.to_index, name="to_index"),
    path("wiki/", views.index, name="index"),
    path("wiki/<str:page>", views.page, name = "page"),
    path("create",views.create_page_view, name = "create"),
    path("edit/<str:pageName>", views.edit_page_view, name = "edit")
]
