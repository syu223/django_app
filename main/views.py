# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock, Karute, Record,MonitoringStock
from .forms import StockForm, RecordForm

# Stock関連のビュー
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'main/stock_list.html', {'stocks': stocks})

def stock_register(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm()
    return render(request, 'main/stock_register.html', {'form': form})

# Karute関連のビュー
def karute_list(request):
    code = request.GET.get('code')
    karutes = Karute.objects.all()
    
    if code:
        karutes = karutes.filter(code=code)

    return render(request, 'main/karute_list.html', {'karutes': karutes})

def karute_detail(request, code):
    karute = get_object_or_404(Karute, code=code)
    records = karute.records.order_by('created_at')  # 日付順に並べ替え
    return render(request, 'main/karute_detail.html', {'karute': karute, 'records': records})

# Record関連のビュー
def record_register(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()  # フォームのデータを保存
            return redirect('karute_list')  # 登録後にKaruteの一覧ページにリダイレクト
    else:
        form = RecordForm()
    return render(request, 'main/record_register.html', {'form': form})

#　監視銘柄のビュー
def monitoring_stocks(request):
    stocks = MonitoringStock.objects.all()
    return render(request, 'main/monitoring_stocks.html', {'stocks': stocks})