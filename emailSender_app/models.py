from django.db import models

# Create your models here.
class Email(models.Model):
    senderEmailAddress = models.EmailField(max_length=30, verbose_name='Sender Email id')
    senderAppPassword = models.CharField(max_length=30, verbose_name='Sender App Password')
    receiverEmailAddress = models.EmailField(max_length=30, verbose_name='Receiver Email id')
    subject = models.CharField(max_length=30, verbose_name='Subject')
    body = models.CharField(max_length=300,verbose_name='Body')