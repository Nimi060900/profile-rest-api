from django.urls import path

from profiles_api import APIViews


urlpatterns = [
path('hello-view/', views.HelloApiView.as_view())
]
