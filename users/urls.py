from django.urls import path

from users.views import LoginAPIView, RegisterAPIView, UserListView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('users/', UserListView.as_view()),
]
