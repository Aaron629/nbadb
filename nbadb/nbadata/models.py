from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Nba_news(models.Model):
  title=models.CharField(db_index=True,default=datetime.strftime(timezone.now(),"%Y%m%d%H%M%S"),max_length=50,verbose_name='標題')
  memo=models.TextField(null=True,blank=True,max_length=3000,verbose_name='內文')
  ldate=models.DateTimeField(db_index=True,default=timezone.now,verbose_name='最後更新時間')
  luser=models.ForeignKey(db_index=True,null=True,blank=True,on_delete=models.CASCADE,verbose_name='最後更新者')
  iobool=models.BooleanField(db_index=True,null=True,default=True,verbose_name='是否有效')
  def __str__(self):
    return u'%s' % (self.title,)
  def save(self,*args,**kwargs):
    self.ldate = timezone.now()
    super(Nba_news,self).save(*args,**kwargs) 
  class Meta:
    verbose_name='news_新聞列表'
    verbose_name_plural=verbose_name