from django.db import models

#銘柄情報のためのテーブル　ここで、銘柄コード、会社名、テーマ、サブコメントを登録
class Stock(models.Model):
    code = models.CharField(max_length=10, unique=True)
    stock_name = models.CharField(max_length=100)
    theme = models.CharField(max_length=200, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.stock_name

#各銘柄に対するカルテのテーブル　code対してのidをrecordテーブルに渡す　
#id、code、company(code)が分かりやすいよう入れている
class Karute(models.Model):
    code = models.CharField(max_length=10)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.company

#karuteテーブルに登録されているodeのidで日々のカルテを管理
class Record(models.Model):
    karute = models.ForeignKey(Karute, related_name='records', on_delete=models.CASCADE)  # Karuteと関連付け
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}: {self.content}"

#監視銘柄テーブル
class MonitoringStock(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
