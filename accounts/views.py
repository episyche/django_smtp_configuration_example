from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import redirect, render

def send_email(request):
    if request.method=="POST":
        email_id = request.POST.get('email_id')
        response_data = "email send to "+email_id
        email_name = email_id.split('@')

        email_template = render_to_string(
            'email.html', {"username": email_name[0]})
        email_obj = EmailMultiAlternatives(
            "Email Notification Example",
            "Email Notification Example",
            settings.EMAIL_HOST_USER,
            [email_id],
        )
        email_obj.attach_alternative(email_template, 'text/html')
        email_obj.send()
        context = {"data":response_data}
        return render(request,"index.html",context)
    else:
        context = {"data":"response_data"}
        return render(request,"index.html")