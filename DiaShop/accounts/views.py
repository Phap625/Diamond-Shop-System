from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from .forms import CustomerForm, LoginForm


def login_customer(request):
    if request.session.get('customer_id'):
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Kiểm tra thông tin đăng nhập trong cơ sở dữ liệu
            with connection.cursor() as cursor:
                cursor.execute("""
                        SELECT * FROM Customer WHERE UserName = %s AND Password = %s
                    """, [username, password])
                customer = cursor.fetchone()

                if customer:
                    # Lưu customer_id vào session và chuyển hướng đến home
                    request.session['customer_id'] = customer[0]
                    return redirect('Home:home')  # Chuyển đến trang home
                else:
                    # Thông báo lỗi nếu không tìm thấy khách hàng
                    messages.error(request, 'Tên đăng nhập hoặc mật khẩu không chính xác.')
        else:
            messages.error(request, 'Vui lòng điền đầy đủ và đúng thông tin.')
    else:
        form = LoginForm()  # Tạo một form trống nếu là GET

    return render(request, 'accounts/login.html', {'form': form})



def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT COUNT(*) FROM Customer WHERE PhoneNumber = %s
                """, [username])
                result = cursor.fetchone()
            if result[0] > 0:
                messages.error(request, "Tên đăng nhập này đã được sử dụng!")
                return render(request, 'accounts/register.html', {'form': form})
            else:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO Customer (UserName,FullName, PhoneNumber, Email, Password, Address)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, [username, full_name, phone_number, email, password, address])

                return redirect('accounts:login')  # Điều hướng sau khi thành công
    else:
        form = CustomerForm()

    return render(request, 'accounts/register.html', {'form': form})


def profile_customer(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('accounts:login')  # Nếu chưa đăng nhập, chuyển hướng đến login

    # Lấy thông tin khách hàng từ cơ sở dữ liệu
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM Customer WHERE CustomerID = %s
        """, [customer_id])
        customer = cursor.fetchone()

    context = {
        'customer': customer
    }
    return render(request, 'accounts/profile.html', context)


def logout_customer(request):
    # Xóa session của khách hàng
    if 'customer_id' in request.session:
        del request.session['customer_id']
    return redirect('Home:home')  # Chuyển về trang chủ