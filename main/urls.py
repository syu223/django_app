# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_list, name='stock_list'),#メイン
    path('register/', views.stock_register, name='stock_register'),#銘柄情報登録用
    path('karute/', views.karute_list, name='karute_list'),  # カルテリスト用
    path('karute/<str:code>/', views.karute_detail, name='karute_detail'),   # カルテ詳細用
    path('record/register/', views.record_register, name='record_register'), #カルテ登録用
    path('monitoring/', views.monitoring_stocks, name='monitoring_stocks'),  # 監視銘柄用
]
