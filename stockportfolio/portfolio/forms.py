from django.forms import ModelForm, TextInput
from .models import Stock 

class StockForm(ModelForm):
    class Meta:
        model = Stock 
        fields = ['name', 'amount']
        widgets = {
        'name' : TextInput(attrs={'class' : 'input is-primary is-rounded', 'placeholder' : 'Stock Ticker'}),
        'amount' : TextInput(attrs={'class' : 'input is-primary is-rounded', 'placeholder' : 'Amount of Shares'})
        }