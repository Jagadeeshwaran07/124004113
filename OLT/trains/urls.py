from django.urls import path
from .views import register_company, obtain_auth_token, get_all_trains

urlpatterns = [
    path('register/', register_company, name='register-company'),
    path('auth/', obtain_auth_token, name='obtain-auth-token'),
    path('trains/', get_all_trains, name='get-all-trains'),
]