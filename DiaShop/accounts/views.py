from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection
from django.contrib import messages
from .forms import CustomerForm, LoginForm

def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Lấy dữ liệu từ form
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT COUNT(*) FROM Customer WHERE PhoneNumber = %s
                """, [phone_number])
                result = cursor.fetchone()
            if result[0] > 0:
                # Nếu số điện thoại đã tồn tại
                messages.error(request, "Số điện thoại này đã được sử dụng!")
                return render(request, 'accounts/register.html', {'form': form})
            else:
            # Chèn dữ liệu vào bảng Customer (không mã hóa mật khẩu)
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO Customer (FullName, PhoneNumber, Email, Password, Address)
                        VALUES (%s, %s, %s, %s, %s)
                    """, [full_name, phone_number, email, password, address])

                return redirect('accounts:login')  # Điều hướng sau khi thành công
    else:
        form = CustomerForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_customer(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        # Kiểm tra trong cơ sở dữ liệu
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM Customer WHERE PhoneNumber = %s AND Password = %s
            """, [phone_number, password])
            customer = cursor.fetchone()

            if customer:
                # Lưu customer_id vào session và chuyển hướng đến home
                request.session['customer_id'] = customer[0]
                return redirect('Home:home')  # Chuyển đến trang home
            else:
                # Nếu không tìm thấy, hiển thị thông báo lỗi
                messages.error(request, 'Số điện thoại hoặc mật khẩu không chính xác.')

    # Chỉ hiển thị form login khi trang được tải hoặc khi có lỗi
    return render(request, 'accounts/login.html')