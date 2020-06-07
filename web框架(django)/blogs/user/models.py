from django.db import models

# Create your models here.
class User(models.Model):
    # title = models.CharField(u'标题', max_length=64)
    name = models.CharField(u'姓名',max_length=30)
    age = models.IntegerField(u'年龄',)
    date_added = models.DateTimeField(u'更新时间',auto_now_add=True)

def _str_(self):
    return  self.text