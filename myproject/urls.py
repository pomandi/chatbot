from django.contrib import admin
from django.urls import path, include
from chatbot import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('chat/', views.chat_view, name='chat_view'),
    path('get_response/', views.get_response, name='get_response'),
]
from django.contrib import admin
from django.urls import path, include
from chatbot import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('chat/', views.chat_view, name='chat_view'),
    path('get_response/', views.get_response, name='get_response'),
]
