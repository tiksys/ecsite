from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import RegistForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


class HomeView(TemplateView):
    template_name = 'home.html'

def regist(request):
    regist_form = RegistForm(request.POST or None)
    if regist_form.is_valid():
        try:
            regist_form.save()
            return redirect('stores:product_list')
        except ValidationError as e:
            regist_form.add_error('password', e)
    return render(
        request, 'regist.html', context={'regist_form': regist_form, }
    )

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm
    print(authentication_form)

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1200000)
        return super().form_valid(form)
"""
def user_login(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('accounts:home')
            else:
                messages.warinng(request, 'ユーザがアクティブではありません')
        else:
            messages.warning(request, 'ユーザかパスワードが間違っています')
    return render(
        request, 'user_login.html', context={
            'login_form': login_form
        }
    )
"""

class UserLogoutView(LogoutView):
    pass


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)