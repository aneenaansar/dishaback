from django.db import models
from ckeditor.fields import RichTextField

APPROVAL = (
    ('Approved','Approved'),
    ('Pending', 'Pending'),
    ('Rejected','Rejected'),
)



STATUS = (
    ('Scheduled','Scheduled'),
    ('Pending', 'Pending'),
    ('Canceled','Canceled'),
)


TIME = (
    ('Morning' , 'Morning'),
    ('Evening','Evening'),
)

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    purpose = models.TextField(max_length=300)
    date = models.DateField()
    status = models.CharField(max_length=50 , choices=STATUS , default='Pending' , blank=True,null=True)
    time = models.CharField(max_length=50 , choices=TIME , blank=True,null=True)


    def __str__(self):
        return self.name


class Blog(models.Model):
        title=models.CharField(max_length=200,null=True)
        content= RichTextField(null=True)
        image=models.ImageField(upload_to='item_images')
        date=models.DateField()


        likes = models.IntegerField(default=0)
        shares = models.IntegerField(default=0)


        def __str__(self):
            return self.title


           