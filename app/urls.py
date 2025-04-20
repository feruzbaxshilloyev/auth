from django.urls import path
from .views import RegisterView, LoginView, ProfilView, ProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profil/', ProfilView.as_view()),
    path('update/', ProfileUpdateView.as_view())
]
