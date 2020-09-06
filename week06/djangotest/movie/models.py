from django.db import models

# Create your models here.

class movieinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    score = models.IntegerField(verbose_name='评分')
    short = models.CharField(max_length=200,verbose_name='影评')
    sentiment = models.FloatField(verbose_name='情感分析')
    start_title = models.CharField(max_length=10,verbose_name='推荐指数')
    class Meta:
        managed = False
        db_table = 'movie_movieinfo'



