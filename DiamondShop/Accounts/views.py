from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # Kiểm tra username đã tồn tại chưa
        if User.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại!")
            print("Tên đăng nhập đã tồn tại!")  # Debug
            return redirect("register")

            # Kiểm tra email đã tồn tại chưa
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email này đã được sử dụng!")
            print("Email đã tồn tại!")  # Debug
            return redirect("register")

        # Kiểm tra mật khẩu có khớp không
        if password1 != password2:
            messages.error(request, "Mật khẩu không khớp!")
            print("Mật khẩu không khớp!")  # Debug
            return redirect("register")

        # Tạo tài khoản nếu hợp lệ
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Đăng ký thành công! Hãy đăng nhập.")
        print("Đăng ký thành công!")  # Debug
        return redirect("login")
    return render(request, "Accounts/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")  # Dùng .get() để tránh lỗi
        password = request.POST.get("password")  # Dùng .get() để tránh lỗi

        if not username or not password:
            messages.error(request, "Vui lòng nhập đầy đủ thông tin!")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Điều hướng đến trang chính sau khi đăng nhập
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng!")

    return render(request, "Accounts/signup_login.html")


def logout_view(request):
    logout(request)
    return redirect('login')
