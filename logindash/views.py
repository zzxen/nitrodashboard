from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
import cryptocompare
from .models import CryptoCurrency , Notes , New , Service , Updates , Alert , Messages
#from coinbase_commerce.client import Client
#from website import settings

# Create your views here.

@login_required(login_url = "signinform")
def main(request):
    btc = cryptocompare.get_price('BTC', currency='USD', full=True)
    btcpricejson = str(btc['RAW']['BTC']['USD']['PRICE'])
    btcprice = str(round(float(btcpricejson)))
    #----------------------------------
    tether = cryptocompare.get_price("USDT" , currency = "USD" , full = True)
    tetherpricejson = str(tether['RAW']["USDT"]['USD']['PRICE'])
    tetherprice = str(round(float(tetherpricejson)))
    #----------------------------------
    etherum = cryptocompare.get_price("ETH" , currency = "USD" , full = True)
    etherumpricejson = str(etherum["RAW"]["ETH"]["USD"]["PRICE"])
    etherumprice = str(round(float(etherumpricejson)))
    #----------------------------------
    etc = cryptocompare.get_price("ETC" , currency = "USD" , full = True)
    etcpricejson = str(etc["RAW"]["ETC"]["USD"]["PRICE"])
    etcprice = str(round(float(etcpricejson)))
    #----------------------------------
    updatess = Updates.objects.all()
    #-----------------------------------
    newss = New.objects.all()
    #-----------------------------------
    servicess = Service.objects.all()
    #-------------------------------------
    alertss = Alert.objects.all()
    #-------------------------------------
    messagess = Messages.objects.all()
    #-------------------------------------
    #client = Client(api_key = settings.COINBASE_COMMERCE_API_KEY)
    #domain_url = "http://127.0.0.1:8080/"
    #product = {"name" : "NitroPlus" , "local_price" : {'amount' : "25" , "currency" : "USD"} , "pricing_type" : "fixed_price" , "redirect_url" : domain_url , "cancel_url" : domain_url + "500err"}
    #chargee = client.charge.create(**product)

    return render(request , "index.html" , {"usdt" : tetherprice , "btc" : btcprice , "eth" : etherumprice , "etc" : etcprice , "newss" : newss , "updates" : updatess , "service" : servicess , "alert" : alertss , "messagee" : messagess})

def loginform(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data["username"] , password = form.cleaned_data["password"])

            if user is not None:
                if user.is_active:
                    login(request , user)
                    return redirect("home")
                else:
                    return redirect("404error")
            else:
                return redirect("404error")
        else:
            messages.error(request , "Login failed. Username or Password incroccet")
    else:
        form = forms.LoginForm()
    
    return render(request , "login.html" , {'form' : form})

def logoutform(request):
    messages.info(request , "Logged out")
    logout(request)
    return redirect("signinform")

def error404(request):
    return render(request , "error-404.html")

def error500(request):
    return render(request , "error-500.html")

def crypto(request):
    cryptoinfo = CryptoCurrency.objects.all()
    notes = Notes.objects.all()
    return render(request , "crypto.html" , context = {"crypto" : cryptoinfo , "notes" : notes})