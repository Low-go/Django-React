from django.urls import path
from .views import roomView

urlpatterns = [

    path('home', roomView.as_view())
]
