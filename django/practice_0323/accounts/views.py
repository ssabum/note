from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import CustomUserChangeForm
from django.contrib.auth import get_user_model

def index(request):
    User = get_user_model()
    users = User.objects.order_by('-pk')
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('notice:index')

    if request.method == 'POST':
        # AuthenticationForm: 사용자가 로그인 할 수 있는 Form
        # 인자로 요청정보 / 사용자가 입력한 아이디, 비밀번호
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            # 세션 CREATE
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'notice:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('notice:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('notice:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('notice:index')
        pass
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('notice:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('notice:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('notice:index')

    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update_password.html', context)
