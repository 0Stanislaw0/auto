from django.urls import path, include
from . import views
from django.contrib.auth import views as authViews

from .router import router

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/signin', views.signin),
    path(r'registration', views.registr, name='reg'),
    path(r'profile/', views.profile, name='profile'),
    path(r'login/', authViews.LoginView.as_view(template_name='users/login.html'), name='login'),

    path(r'pass-reset/',
         authViews.PasswordResetView.as_view(template_name='users/pass_reset.html'), name='pass-reset'),

    path(r'password-reset-confirm/<uidb64>/<token>/',
         authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path(r'password-reset/done/',
         authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path(r'password-reset-complete/',
         authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path(r'exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
]
