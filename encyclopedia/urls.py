from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hope_no_one_ever_enters_this", views.search, name="search"),
    path("<str:entry>", views.entry_page, name="entry_page")
]
