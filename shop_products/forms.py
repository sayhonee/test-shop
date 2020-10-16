from django import forms
from django.core import validators


class PostForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput
        (attrs={"placeholder": "لطفا نام خود را وارد کنید", "class": "form-control"}),
        label="نام و نام خانوادکی",
        validators=[
            validators.MaxLengthValidator(20, message="بیشتر از حد مجاز"),
            validators.MinLengthValidator(5, message="کمتر از حد مجاز")
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput
        (attrs={"placeholder": "لطفا ایمیل خود را وارد کنید", "class": "form-control"}),
        label="ایمیل",
        validators=[
            validators.MaxLengthValidator(100, message="بیشتر از حد مجاز")

        ]
    )


    text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": " لطفا پیام خود را وارد کنید", "row": 8}),
        label="پیغام",

    )
