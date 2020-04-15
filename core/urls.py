from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.auth.views import *

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('detail/<int:pk>', views.HomeDetailListView.as_view(), name='detail_page'),
    path('account/<int:pk>', views.AccountDetailListView.as_view(), name='account_page'),
    path('edit-page', views.CustomersCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', views.CustomersUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.CustomersDeleteView.as_view(), name='delete_page'),
    path('login', views.AuthorizationLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.ProjectLogout.as_view(), name='logout_page'),
    path('password-change', views.ChangePasswordLoginView.as_view(), name='password_change_page'),
    path('password-change-done', views.ChangePasswordDoneView.as_view(), name='password_change_done'),
    path('password-reset-form', views.ResetPasswordView.as_view(), name='password_reset_form'),
    path('password-reset-done', views.ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', views.ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete', views.ResetPasswordCompleteView.as_view(), name='password_reset_complete'),
]
