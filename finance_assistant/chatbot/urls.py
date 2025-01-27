from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    # path('response/', views.response_ai, name='response_ai'),
]
