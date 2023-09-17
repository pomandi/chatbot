from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat_view'),
    path('get_response/', views.get_response, name='get_response'),
]
