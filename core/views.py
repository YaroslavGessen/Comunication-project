from django.shortcuts import render, redirect
from .models import Customers
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import CustomersForm, AuthUserForm, RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeListView(LoginRequiredMixin,ListView):
    model = Customers
    template_name = "index.html"
    context_object_name = 'list_customers'

class HomeDetailListView(LoginRequiredMixin,DetailView):
    model = Customers
    template_name = "detail.html"
    context_object_name = 'get_customer'



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

class RegisterUserView(CreateView):
    model = User
    template_name = "registration_page.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')
    success_msg = 'User was created successfully'
    
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid

class ProjectLogout(LogoutView):
    next_page = reverse_lazy('login_page')