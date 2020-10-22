from django.urls import path
from productos import views

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view() )
]
