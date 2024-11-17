from django import forms
from .models import Stock,Karute,Record

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['code', 'stock_name', 'theme', 'comments']

class KaruteForm(forms.ModelForm):
    class Meta:
        model = Karute
        fields = ['code', 'company']

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['karute', 'content'] 