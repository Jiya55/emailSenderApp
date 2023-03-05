from django.shortcuts import render
# Create your views here.
from django.template import loader
from django.http import HttpResponse
from .forms import  EmailForm 
from .senderbot import email_sender_bot
def home(request):
  template = loader.get_template("emailSender_app/index.html")
  return HttpResponse(template.render())

def base(request):
  template = loader.get_template("emailSender_app/base.html")
  return HttpResponse(template.render())

def test(request):
  template = loader.get_template("emailSender_app/test.html")
  return HttpResponse(template.render())

def thankYoupage(request):
  template = loader.get_template("emailSender_app/ThankYouPage.html")
  return HttpResponse(template.render())

def send_email(request):
  if request.method == "GET":
    form = EmailForm
    return render(request, 'emailSender_app/emailCreateForm.html', {'form': form})
  if request.method == "POST":
    MyEmailForm = EmailForm(request.POST)
    if MyEmailForm.is_valid():
      senderEmailAddress = MyEmailForm.cleaned_data['senderEmailAddress']
      senderAppPassword= MyEmailForm.cleaned_data['senderAppPassword']
      receiverEmailAddress= MyEmailForm.cleaned_data['receiverEmailAddress']
      subject= MyEmailForm.cleaned_data['subject']
      body= MyEmailForm.cleaned_data['body']
      email_sender_bot(senderEmailAddress,senderAppPassword,receiverEmailAddress,subject,body)
      return render(request, 'emailSender_app/ThankYouPage.html')
    else:
      return render(request, 'emailSender_app/index.html')