from django.shortcuts import render, redirect
import requests
from .models import Stock
from .forms import StockForm

def index(request):
	url = "https://finnhub.io/api/v1/quote?symbol={}&token=c36cckiad3ifoi8hn8fg"

	err_msg = ''

	if request.method == 'POST':
		form = StockForm(request.POST)
		if form.is_valid():
			new_stock = form.cleaned_data['name']
			existing_city_count = Stock.objects.filter(name = new_stock).count()
			if (existing_city_count == 0):
				r = requests.get(url.format(new_stock)).json()
				form.save()
			else:
				err_msg = 'Stock already added to portfolio'

	form = StockForm()

	stocks = Stock.objects.all()

	stock_data = []

	for stock in stocks:

		r = requests.get(url.format(stock)).json()

		stock_attributes = {
			'name' : stock.name,
			'price' : round(r['c'],2),
			'amount' : stock.amount,
			'totalShare' : round((r['c']*stock.amount),2),

		}

		stock_data.append(stock_attributes)

	totalPrice = 0

	for stock_attributes in stock_data:
		totalPrice += stock_attributes["totalShare"]
	totalPrice = round(totalPrice, 2)

	context = {'stock_data': stock_data, 'form':form, 'totalPrice': totalPrice}


	return render(request,'portfolio/index.html', context)

def delete_stock(request, stock_name):
	Stock.objects.get(name = stock_name).delete()
	return redirect('home')