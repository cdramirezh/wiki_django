from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_new_page", views.new_page, name="new_page"),
    path("hope_no_one_ever_enters_this", views.search, name="search"),
    path("<str:entry>", views.entry_page, name="entry_page")
]
