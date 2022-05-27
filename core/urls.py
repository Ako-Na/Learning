from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views 

urlpatterns = [
    # Authentication
    path('token-auth', obtain_auth_token, name="api_token_auth"),
    # path('create-account', views.Account.as_view(), name="create_account"),

    # User Profile
    path('profile', views.Profile.as_view(), name="profile")
]