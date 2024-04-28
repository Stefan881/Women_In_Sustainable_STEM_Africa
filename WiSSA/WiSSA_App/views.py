from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# Create your views here.
def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email =  request.POST['email']
        message = request.POST['message']

        # function to send the email
        send_mail(
            message_name,
            message,
            message_email,
            ['ondeyostephen0@gmail.com']
        )
        return render(request,'contact.html',{'message_name':message_name})
    return render(request,'contact.html')

def news(request):
    return render(request,'news.html',{})

def support_us(request):
    return render(request,'support_us.html',{})








