from django.db import models

# Create your models here.
class EmpInfo(models.Model):
    username = models.CharField(blank=False,max_length=25)
    email = models.EmailField(blank=False,max_length=25)
    password_first = models.CharField(blank=False, max_length=25)
    password_again = models.CharField(blank=False, max_length=25)
    def __str__(self):
        return self.username


class Blog(models.Model):
    title= models.CharField(blank=False, max_length=100)
    content= models.CharField(blank=False, max_length=100000)
    pub_date= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
