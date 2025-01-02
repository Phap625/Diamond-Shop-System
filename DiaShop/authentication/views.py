from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Đăng ký thành công! Xin chào, {}.".format(user.username))
            return redirect('home')  # Chuyển đến trang chính sau khi đăng nhập
        else:
            messages.error(request, "Đăng ký không thành công. Vui lòng kiểm tra lại thông tin.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Đăng nhập thành công! Xin chào, {}.".format(user.username))
                return redirect('home')  # Chuyển đến trang chính sau khi đăng nhập
        else:
            messages.error(request, "Đăng nhập không thành công. Vui lòng kiểm tra tên đăng nhập và mật khẩu.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})