from django.urls import re_path
from .views import BookView


app_name = "api"

urlpatterns = [
    re_path(r'^books/$', BookView.as_view(), name='book-list'),
]

