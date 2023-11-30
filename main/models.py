from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    purpose = models.TextField(max_length=300)
    date = models.DateField()


    def __str__(self):
        return self.name
    
class Blog(models.Model):
    date = models.DateField()
    heading = models.CharField(max_length=255)
    paragraph = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images')
    h1 = models.CharField(max_length=255,blank=True)
    p1 = models.CharField(max_length=255,blank=True)
    h2 = models.CharField(max_length=255,blank=True)
    p2 = models.CharField(max_length=255,blank=True)
    h3 = models.CharField(max_length=255,blank=True)
    p3 = models.CharField(max_length=255,blank=True)
    p4 = models.CharField(max_length=255,blank=True)
    p5 = models.CharField(max_length=255,blank=True)
    p6 = models.CharField(max_length=255,blank=True)
    p7 = models.CharField(max_length=255,blank=True)
    p8 = models.CharField(max_length=255,blank=True)
    p9 = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.heading
    