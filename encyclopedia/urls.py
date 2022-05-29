from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_new_page/create", views.new_page, name="new_page"),
    path("hope_no_one_ever_enters_this/search", views.search, name="search"),
    path("edit_page/<str:entry>", views.edit_page, name="edit_page"),
    path("<str:entry>", views.entry_page, name="entry_page"),
    path("random_page/random", views.random_page, name="random_page")
]
