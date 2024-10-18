from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.chat, name='chat'),  # This will render chat.html
]




