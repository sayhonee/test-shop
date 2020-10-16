from django.shortcuts import render
from .forms import ContactForm
from .models import ContactUs


# Create your views here.


def contactpage(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get("full_name")
        email = contact_form.cleaned_data.get("email")
        subject = contact_form.cleaned_data.get("subject")
        text = contact_form.cleaned_data.get("text")
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        # todo : show user a success message
        contact_form = ContactForm
    context = {
        "contact_form": contact_form
    }
    return render(request, "contactus/contactus.html", context)
