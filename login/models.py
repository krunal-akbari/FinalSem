from django.db import models

# Create your models here.
class CustomerModel(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=40)
    address1 = models.CharField(max_length=60,null=True, blank=True)
    address2 = models.CharField(max_length=60,null=True, blank=True)
    city = models.CharField(max_length=15,null=True, blank=True)
    phoneno = models.CharField(max_length=10,null=True, blank=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=40,null=True, blank=True)

    def __str__(self):
        return f"{self.cname}"
