from django.contrib import admin
from django.urls import path, include
from core import views

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
]
