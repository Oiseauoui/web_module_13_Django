from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .views import RegisterView, SignInView, ResetPasswordView
from django.urls import path

app_name = "users"

urlpatterns = [
    path("signup/", RegisterView.as_view(), name='register'),
    path("signin/", SignInView.as_view(template_name='users/signin.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("password_reset/", ResetPasswordView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),
    # path('profile/', profile_view(template_name='users/profile.html'), name='profile'),
    path("password_reset/done/", PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path("password_reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                                                                      success_url='/users/reset-password/complete/'), name='password_reset_confirm'),
    path("password_reset/complete/", PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
