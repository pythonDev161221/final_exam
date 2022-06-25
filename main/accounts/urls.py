from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import login_view, logout_view

app_name = "accounts"

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('accounts/login/', LoginView.as_view(), name='login'),
    # path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
