from django.contrib import admin
from django.urls import path

from .views import LocationAPIVIEW, UserView, WorktypeAPIVIEW

urlpatterns = [
    path("location", LocationAPIVIEW.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path("location/<str:pk>", LocationAPIVIEW.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy'
        }
    )),
    path("worktype", WorktypeAPIVIEW.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path("worktype/<str:pk>", WorktypeAPIVIEW.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy'
        }
    )),
    path("user", UserView.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path("user/<str:pk>", UserView.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy'
        }
    )),
]