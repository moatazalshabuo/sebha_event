from django.db import models

# Create your models here.
class BesicData(models.Model):
    title = models.CharField(max_length=125)
    from_date = models.DateField()
    to_date = models.DateField(null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    
class Organizers(models.Model):
    name = models.CharField(max_length=150)
    pic = models.ImageField(upload_to='Organizers/%Y/%m/%d/')
    face_link = models.CharField(max_length=125,null=True,blank=True)
    x_link = models.CharField(max_length=125,null=True,blank=True)
    web_site = models.CharField(max_length=125,null=True,blank=True)
    phone = models.CharField(max_length=125,null=True,blank=True)
    
    def get_img(self):
        if self.pic:
            return 'http://127.0.0.1:8000/'+self.pic.url
        
class Shepherds(models.Model):
    name = models.CharField(max_length=150)
    pic = models.ImageField(upload_to='Shepherds/%Y/%m/%d/')
    face_link = models.CharField(max_length=125,null=True,blank=True,default='')
    x_link = models.CharField(max_length=125,null=True,blank=True,default='')
    web_site = models.CharField(max_length=125,null=True,blank=True,default='')
    type = models.CharField(max_length=125,choices=(('gold','gold'),('silver','silver'),('bronze','bronze')))
    
    def get_img(self):
        if self.pic:
            return 'http://127.0.0.1:8000/'+self.pic.url
        

class Schedule(models.Model):
    title = models.CharField(max_length=120)
    descripe = models.TextField(null=True,blank=True,default='لم يتم اضافة تفاصيل ')
    from_time = models.CharField(max_length=6)
    to_time = models.CharField(max_length=6)
    day = models.DateField()
    
    
    
class Speakers(models.Model):
    name = models.CharField(max_length=150)
    pic = models.ImageField(upload_to='Speakers/%Y/%m/%d/')
    type = models.CharField(max_length=125,null=True,blank=True,default='')
    
    def get_img(self):
        if self.pic:
            return 'http://127.0.0.1:8000/'+self.pic.url
        