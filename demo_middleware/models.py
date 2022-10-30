from django.db import models

# Create your models here.

#!NewStats
class NewStats(models.Model):
    win = models.IntegerField()#windows
    mac = models.IntegerField()#mac
    iph = models.IntegerField()#iphone
    android = models.IntegerField()#android
    oth = models.IntegerField()#other computer os system or telephone os system  
    
    def __str__(self):
        return 'Operating System'
    
    class Meta:
        verbose_name = 'NewStat'
        verbose_name_plural = 'NewStats'
    
    
    