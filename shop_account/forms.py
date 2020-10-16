from django import forms
from django.contrib.auth.models import User
from django.core import validators


class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام خود را وارد کنید","class":"form-control"}),
        label="نام")

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام خانوادگی خود را وارد کنید","class":"form-control"}),
        label="نام خانوادگی")






class LoginForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "لطفا نام کاربری خود را وارد کنید"}),
                                label="نام کاربری")

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا رمز خود را وارد کنید"}),
        label="کلمه عبور"
    )

    # def clean_user_name(self):
    #     user_name = self.cleaned_data.get("user_name")
    #     is_exists_user = User.objects.filter(username=user_name).exists()
    #     if not is_exists_user:
    #         raise forms.ValidationError("نام کاربری یا کلمه عبور اشتباه است")
    #     return user_name


class RegisterForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "لطفا نام کاربری خود را وارد کنید"}),
                                label="نام کاربری",
                                validators=[
                                    validators.MaxLengthValidator(limit_value=20, message="بیشتر از حد مجاز"),
                                    validators.MinLengthValidator(5, message="کمتر از حد مجاز")
                                ])

    email = forms.CharField(widget=forms.EmailInput
    (attrs={"placeholder": "لطفا ایمیل خود را وارد کنید"}),
                            label="ایمیل",
                            validators=[validators.EmailValidator("ایمیل وارد شده صحیح نمی باشد")]
                            )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "لطفارمز عبور خود را وارد کنید"}
        ),
        label="رمز عبور ",
        validators=[
            validators.MaxLengthValidator(limit_value=30, message="بیشتر از حد مجاز"),
            validators.MinLengthValidator(5, message="کمتر  از حد مجاز"),

        ])

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "لطفارمز تایید عبور خود را وارد کنید"}),
        label="رمز تایید"
    )

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if password != re_password:
            raise forms.ValidationError("کلمه عبور یکسان نیست")
        else:
            return password

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError("کاربری با همین نام وجود دارد")
        else:
            return user_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        is_exists_user_by_email = User.objects.filter(username=email).exists()

        if is_exists_user_by_email:
            raise forms.ValidationError("ایمیل وارد شده تکراری می باشد")
