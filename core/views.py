from django.shortcuts import render, redirect
from .models import Customers
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import CustomersForm, AuthUserForm, RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.password_validation import *
from django.contrib.auth.forms import PasswordChangeForm

class HomeListView(LoginRequiredMixin,ListView):
    model = Customers
    template_name = "index.html"
    context_object_name = 'list_customers'

class HomeDetailListView(LoginRequiredMixin,DetailView):
    model = Customers
    template_name = "detail.html"
    context_object_name = 'get_customer'

class AccountDetailListView(LoginRequiredMixin,DetailView):
    model = User
    template_name = "account_page.html"
    context_object_name = 'get_account'

class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False
        
    def form_valid(self,form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)
    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class CustomersCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    model = Customers
    template_name = 'edit_page.html'
    form_class = CustomersForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Customers added successfully'
    def get_context_data(self,**kwargs):
        kwargs['list_customers'] = Customers.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class CustomersUpdateView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Customers
    template_name = 'edit_page.html'
    form_class = CustomersForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Updated successfully'
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class CustomersDeleteView(LoginRequiredMixin, DeleteView):
    model = Customers
    template_name = 'edit_page.html'
    success_url = reverse_lazy('edit_page')
    success_msg = 'Customer was deleted successfully'
    
    def post(self,request,*args,**kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

class AuthorizationLoginView(LoginView):
    template_name = "login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')
    def get_success_url(self):
        return self.success_url

class ChangePasswordLoginView(LoginRequiredMixin,PasswordChangeView):
    template_name = "change_password_page.html"
    form_class = PasswordChangeForm
    success_msg = 'Password was changed successfully'
    success_url = reverse_lazy('password_change_done')
    def get_success_url(self):
        return self.success_url

class ChangePasswordDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = "password_change_done.html"
    success_msg = 'Password change successful'
    
class ResetPasswordView(PasswordResetView):
    email_template_name = 'password_reset_email.html'
    template_name = "password_reset_form.html"
    subject_template_name = 'password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'

class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

class RegistrationCompleteView(PasswordResetCompleteView):
    template_name = 'registration_complete.html'

class RegisterUserView(CreateView):
    model = User
    template_name = "registration_page.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('registration_complete')
    success_msg = 'User was created successfully'
    
    # def form_valid(self, form):
    #     form_valid = super().form_valid(form)
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password1']
    #     aut_user = authenticate(username=username, password=password)
    #     login(self.request, aut_user)
    #     return form_valid
    #problems with axes login

class ProjectLogout(LogoutView):
    next_page = reverse_lazy('login_page')