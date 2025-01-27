from django.shortcuts import render, redirect
from django.contrib import messages
import random, logging
from .models import Customer
from .forms import CustomerForm, LoginForm, UpdateCustomerForm
from django.utils.safestring import mark_safe
from django.urls import reverse


logger = logging.getLogger('otp')


def send_otp(phone_number):
    otp = random.randint(100000, 999999)  # Tạo mã OTP 6 chữ số
    logger.info(f"Mã OTP cho số điện thoại {phone_number}: {otp}")  # Hiển thị OTP trên console
    return otp


def login_customer(request):
    # Nếu người dùng đã đăng nhập, chuyển hướng đến trang profile
    if request.session.get('customer_id'):
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_phone = form.cleaned_data['username']
            password = form.cleaned_data['password'].strip()

            try:
                if username_or_phone.isdigit():
                    customer = Customer.objects.get(phone_number=username_or_phone)
                else:
                    customer = Customer.objects.get(username=username_or_phone)
            except Customer.DoesNotExist:
                messages.error(request, 'Tên đăng nhập hoặc số điện thoại không tồn tại.')
                return redirect('accounts:login')

            if password != customer.password:
                reset_password_url = reverse('accounts:reset_password')  # Lấy URL của reset_password
                messages.error(
                    request,
                    mark_safe(f"Mật khẩu không chính xác. <a href='{reset_password_url}'>Bạn quên mật khẩu?</a>")
                )
                return redirect('accounts:login')

            # Đăng nhập thành công: lưu customer_id vào session
            request.session['customer_id'] = customer.id
            return redirect('Home:home')
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

            if Customer.objects.filter(username=username).exists():
                messages.error(request, "Tên đăng nhập này đã được sử dụng!")
                return render(request, 'accounts/register.html', {'form': form})

            if Customer.objects.filter(phone_number=phone_number).exists():
                messages.error(request, "Số điện thoại này đã được đăng ký!")
                return render(request, 'accounts/register.html', {'form': form})


            customer = Customer.objects.create(
                username=username,
                full_name=full_name,
                phone_number=phone_number,
                email=email,
                password=password,
                address=address,
            )

            # Gửi OTP
            otp = send_otp(phone_number)
            request.session['otp'] = otp
            request.session['phone_number'] = phone_number

            messages.success(request, f'Mã OTP đã được gửi đến {phone_number}. Vui lòng kiểm tra terminal.')

            return redirect('accounts:verify_otp')
    else:
        form = CustomerForm()

    return render(request, 'accounts/register.html', {'form': form})


def profile_customer(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('accounts:login')

    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        request.session.flush()
        return redirect('accounts:login')

    # Truyền thông tin khách hàng vào context
    context = {
        'customer': customer
    }
    return render(request, 'accounts/profile.html', context)


def logout_customer(request):
    request.session.flush()
    messages.success(request, "Bạn đã đăng xuất thành công.")
    return redirect('Home:home')


def update_customer_info(request):
    if not request.session.get('customer_id'):
        return redirect('accounts:login')  # Yêu cầu đăng nhập nếu chưa đăng nhập

    customer_id = request.session['customer_id']  # Lấy ID khách hàng từ session

    try:
        # Lấy đối tượng khách hàng từ cơ sở dữ liệu
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        messages.error(request, "Không tìm thấy thông tin khách hàng.")
        return redirect('accounts:login')

    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST)
        if form.is_valid():
            # Lấy dữ liệu từ form
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']

            # Kiểm tra mật khẩu
            if password == customer.password:  # So sánh trực tiếp (không mã hóa)
                # Cập nhật thông tin khách hàng
                if Customer.objects.filter(phone_number=phone_number).exclude(id=customer_id).exists():
                    messages.error(request, "Số điện thoại đã được liên kết với một tài khoản khác.")
                else:
                    # Cập nhật thông tin khách hàng
                    customer.full_name = full_name
                    customer.phone_number = phone_number
                    customer.email = email
                    customer.address = address
                    customer.save()  # Lưu thay đổi vào cơ sở dữ liệu

                    messages.success(request, "Cập nhật thông tin thành công!")
                    return redirect('accounts:profile')  # Chuyển hướng đến trang profile
            else:
                messages.error(request, "Mật khẩu không đúng. <a href='{}'>Bạn quên mật khẩu?</a>".format(
                    reverse('accounts:reset_password')))
        else:
            messages.error(request, "Vui lòng điền đầy đủ thông tin hợp lệ.")
    else:
        # Khởi tạo form với thông tin hiện tại của khách hàng
        form = UpdateCustomerForm(initial={
            'full_name': customer.full_name,
            'phone_number': customer.phone_number,
            'email': customer.email,
            'address': customer.address,
        })

    return render(request, 'accounts/update_info.html', {'form': form})


def verify_otp(request):
    # Kiểm tra nếu mã OTP không tồn tại trong session
    if 'otp' not in request.session or 'phone_number' not in request.session:
        messages.error(request, 'Không tìm thấy mã OTP hoặc số điện thoại. Vui lòng thực hiện lại quá trình đăng ký.')
        return redirect('accounts:register')  # Chuyển hướng về trang đăng ký

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        saved_otp = request.session.get('otp')

        if not entered_otp:
            messages.error(request, 'Vui lòng nhập mã OTP.')
        elif str(entered_otp).strip() == str(saved_otp).strip():
            messages.success(request, 'Số điện thoại đã được xác minh thành công!')

            # Xóa OTP khỏi session sau khi xác minh thành công
            request.session.pop('otp', None)

            if request.session.get('reset_password', False):
                request.session.pop('reset_password', None)  # Xóa cờ reset_password
                return redirect('accounts:update_password')

            request.session.pop('phone_number', None)
            return redirect('accounts:login')
        else:
            messages.error(request, 'Mã OTP không đúng. Vui lòng thử lại.')

    return render(request, 'accounts/verify_otp.html')


def reset_password(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')

        # Kiểm tra số điện thoại có tồn tại trong cơ sở dữ liệu không
        try:
            customer = Customer.objects.get(phone_number=phone_number)
        except Customer.DoesNotExist:
            messages.error(request, 'Số điện thoại này không được đăng ký.')
            return redirect('accounts:reset_password')

        # Nếu số điện thoại tồn tại, tạo mã OTP và lưu vào session
        otp = send_otp(phone_number)
        request.session['otp'] = otp
        request.session['phone_number'] = phone_number
        request.session['reset_password'] = True  # Đánh dấu cờ reset_password

        messages.success(request, f'Mã OTP đã được gửi đến {phone_number}. Vui lòng kiểm tra terminal.')
        return redirect('accounts:verify_otp')  # Chuyển hướng đến trang xác minh OTP

    return render(request, 'accounts/reset_password.html')


def update_password(request):
    if 'phone_number' not in request.session:
        messages.error(request, 'Không tìm thấy thông tin cần thiết. Vui lòng thử lại.')
        return redirect('accounts:reset_password')

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not new_password or not confirm_password:
            messages.error(request, 'Vui lòng điền đầy đủ thông tin.')
            return redirect('accounts:update_password')

        if new_password != confirm_password:
            messages.error(request, 'Mật khẩu không khớp. Vui lòng thử lại.')
            return redirect('accounts:update_password')

        # Cập nhật mật khẩu mới
        phone_number = request.session.get('phone_number')
        try:
            customer = Customer.objects.get(phone_number=phone_number)
            customer.password = new_password  # Lưu trực tiếp mật khẩu
            customer.save()

            # Xóa session phone_number
            request.session.pop('phone_number', None)

            messages.success(request, 'Mật khẩu đã được cập nhật thành công! Vui lòng đăng nhập.')
            return redirect('accounts:login')
        except Customer.DoesNotExist:
            messages.error(request, 'Không tìm thấy tài khoản tương ứng. Vui lòng thử lại.')
            return redirect('accounts:reset_password')

    return render(request, 'accounts/update_password.html')