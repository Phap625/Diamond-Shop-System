from django import forms

class CustomerForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True, label="Họ và Tên")
    phone_number = forms.CharField(max_length=15, required=True, label="Số Điện Thoại")
    email = forms.EmailField(max_length=100, required=True, label="Email")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Mật khẩu")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Xác nhận mật khẩu")
    address = forms.CharField(max_length=200, required=True, label="Địa chỉ")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Mật khẩu và xác nhận mật khẩu không khớp.")

        return cleaned_data

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)