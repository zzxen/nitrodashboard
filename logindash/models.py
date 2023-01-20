from django.db import models


class CryptoCurrency(models.Model):
    name = models.CharField(max_length = 100 , blank = False , default = "Contact us from telegram @nitrosupport24h")
    wallet_address = models.TextField(default = "Contact us from telegram @nitrosupport24h")

class Notes(models.Model):
    note = models.TextField(default = "Contact us from telegram @nitrosupport24h")

class New(models.Model):
    news = models.CharField(max_length = 240 , blank = False , default = "Not any News yet")

class Updates(models.Model):
    updatee = models.CharField(max_length = 240 , blank = False , default = "Not any Updates yet")

class Service(models.Model):
    service_name = models.CharField(max_length = 50 , blank = False , default = "Not service available yet")
    service_price = models.CharField(max_length = 50 , blank = False , default = "-")
    options = models.TextField(default = "Not service available yet")

class Alert(models.Model):
    alert_body = models.CharField(max_length = 240 , blank = False , default = "After paid for service sent it from telegram")

class Messages(models.Model):
    message_body = models.CharField(max_length = 240 , blank = False , default = "Thanks for your registration")