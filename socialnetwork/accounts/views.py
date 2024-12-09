from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import UserRegisterForm, CustomLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            messages.success(request, 'Account created successfully', 'success')
            return redirect("home:home")

        messages.error(request, 'Something went wrong', 'danger')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in', 'success')
                return redirect("home:home")
            else:
                messages.error(request, 'username or password is wrong !!!', 'danger')
                return redirect("accounts:login")

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You are now logged out', 'success')
        return redirect("home:home")

























