from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
import random, logging, time
from .forms import CustomerForm, LoginForm, UpdateCustomerForm


logger = logging.getLogger('otp')


def send_otp(phone_number):
    otp = random.randint(100000, 999999)  # Tạo mã OTP 6 chữ số
    logger.info(f"Mã OTP cho số điện thoại {phone_number}: {otp}")  # Hiển thị OTP trên console
    return otp


def login_customer(request):
    if request.session.get('customer_id'):
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Kiểm tra xem username có tồn tại trong cơ sở dữ liệu hay không
            with connection.cursor() as cursor:
                cursor.execute("SELECT CustomerID, Password FROM Customer WHERE UserName = %s", [username])
                customer = cursor.fetchone()

                if not customer:
                    # Nếu username không tồn tại
                    messages.error(request, 'Tên đăng nhập không tồn tại.')
                    return redirect('accounts:login')
                else:
                    # Kiểm tra mật khẩu
                    stored_password = customer[1]
                    if password != stored_password:
                        messages.error(request, "Mật khẩu không chính xác. <a href='{% url 'accounts:reset_password' %}'>Bạn quên mật khẩu?</a>")
                    else:
                        # Lưu customer_id vào session và chuyển hướng đến home
                        request.session['customer_id'] = customer[0]
                        return redirect('Home:home')  # Chuyển đến trang home
        else:
            messages.error(request, 'Vui lòng điền đầy đủ và đúng thông tin.')
    else:
        form = LoginForm()

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
                    SELECT COUNT(*) FROM Customer WHERE Username = %s
                """, [username])
                result = cursor.fetchone()
            if result[0] > 0:
                messages.error(request, "Tên đăng nhập này đã được sử dụng!")
                return render(request, 'accounts/register.html', {'form': form})

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT COUNT(*) FROM Customer WHERE PhoneNumber = %s
                """, [phone_number])
                result = cursor.fetchone()

            if result[0] > 0:
                messages.error(request, "Số điện thoại này đã được đăng ký!")
                return render(request, 'accounts/register.html', {'form': form})
            else:
                with connection.cursor() as cursor:
                    cursor.execute("""
                                        INSERT INTO Customer (UserName, FullName, PhoneNumber, Email, Password, Address)
                                        VALUES (%s, %s, %s, %s, %s, %s)
                                    """, [username, full_name, phone_number, email, password, address])

                otp = send_otp(phone_number)
                request.session['otp'] = otp
                request.session['phone_number'] = phone_number

                messages.success(request, f'Mã OTP đã được gửi đến {phone_number}. Vui lòng kiểm tra console.')

                return redirect('accounts:verify_otp')
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


def update_customer_info(request):
    if not request.session.get('customer_id'):
        return redirect('accounts:login')  # Yêu cầu đăng nhập nếu chưa đăng nhập

    customer_id = request.session['customer_id']

    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']

            # Xác thực mật khẩu
            with connection.cursor() as cursor:
                cursor.execute("SELECT Password FROM Customer WHERE CustomerID = %s", [customer_id])
                stored_password = cursor.fetchone()

                if stored_password and stored_password[0] == password:  # Kiểm tra mật khẩu
                    # Cập nhật thông tin khách hàng
                    cursor.execute("""
                        UPDATE Customer
                        SET FullName = %s, PhoneNumber = %s, Email = %s, Address = %s
                        WHERE CustomerID = %s
                    """, [full_name, phone_number, email, address, customer_id])
                    messages.success(request, "Cập nhật thông tin thành công!")  # Gửi thông báo thành công
                    return redirect('accounts:profile')  # Chuyển hướng đến trang profile
                else:
                    messages.error(request, "Mật khẩu không đúng. <a href='{% url 'accounts:reset_password' %}'>Bạn quên mật khẩu?</a>")
        else:
            messages.error(request, "Vui lòng điền đầy đủ thông tin hợp lệ.")
    else:
        # Lấy thông tin khách hàng hiện tại để hiển thị trên form
        with connection.cursor() as cursor:
            cursor.execute("SELECT FullName, PhoneNumber, Email, Address FROM Customer WHERE CustomerID = %s", [customer_id])
            customer = cursor.fetchone()

        form = UpdateCustomerForm(initial={
            'full_name': customer[0],
            'phone_number': customer[1],
            'email': customer[2],
            'address': customer[3],
        })

    return render(request, 'accounts/update_info.html', {'form': form})


def verify_otp(request):
    # Kiểm tra nếu mã OTP không tồn tại trong session
    if 'otp' not in request.session:
        messages.error(request, 'Không tìm thấy mã OTP. Vui lòng thực hiện lại quá trình đăng ký.')
        return redirect('accounts:register')  # Chuyển hướng về trang đăng ký

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        saved_otp = request.session.get('otp')

        if str(entered_otp) == str(saved_otp):
            messages.success(request, 'Số điện thoại đã được xác minh thành công!')

            # Xóa OTP khỏi session sau khi xác minh thành công
            del request.session['otp']
            del request.session['phone_number']

            return redirect('accounts:login')
        else:
            messages.error(request, 'Mã OTP không đúng. Vui lòng thử lại.')

    return render(request, 'accounts/verify_otp.html')


def ForgotPass(request):
    return render(request, 'accounts/ForgotPass.html')

