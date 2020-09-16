from django.shortcuts import render
import requests
import json

# Create your views here.


def home(request):
    #  grab price
    price_request = requests.get(
        'https://min-api.cryptocompare.com/data/pricemultifull?'
        'fsyms=BTC,XRP,ETH,EOS,LTC,BCH,XLM,IOT,DASH,ETC,ZEC,OMG,BTT&tsyms=USD,INR'
    )
    price = json.loads(price_request.content)
    #  grab news
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote'].upper()
        quote = ' '.join(quote.split())
        quote = quote.replace(' ', ',')
        crypto_request = requests.get(
            'https://min-api.cryptocompare.com/data/pricemultifull?'
            'fsyms=' + quote + '&tsyms=USD,INR'
        )
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
    else:
        notfound = 'Enter a cryptocurrency symbol above in search bar ...'
        return render(request, 'prices.html', {'notfound': notfound})


def about(request):
    return render(request, 'about.html')



