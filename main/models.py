from django.db import models
from ckeditor.fields import RichTextField
# from django.contrib.auth.models import User

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
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    purpose = models.TextField(max_length=300)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS, default='Pending', blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    # approval = models.CharField(max_length=50, choices=APPROVAL, default='Pending')

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=200,null=True)
    content= RichTextField(null=True)
    image=models.ImageField(upload_to='item_images')
    date=models.DateField()
    is_featured=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    review=RichTextField(null=True)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
           