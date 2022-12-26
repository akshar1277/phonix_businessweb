from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Contact(models.Model):
    first_name=models.CharField(max_length=150,null=True)
    last_name=models.CharField(max_length=150,null=True)
    company=models.CharField(max_length=150,null=True)
    email=models.EmailField(max_length = 254,null=True)
    phone=models.IntegerField(blank=True, null=True)
    interested_in=models.CharField(max_length=150,null=True)
    estimated_budget=models.CharField(max_length=150,null=True)
    project_timeline=models.CharField(max_length=150,null=True)
    about_us=models.CharField(max_length=150,null=True)
    description=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
    
class Positions(models.Model):
    name=models.CharField(max_length=150,null=True)
    email=models.EmailField(max_length = 254,null=True)
    phone=models.IntegerField(blank=True, null=True)
    portfolio_url=models.URLField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Job positions"
        verbose_name_plural = "Job positions"
