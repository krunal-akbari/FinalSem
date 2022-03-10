from django.db import models
from home.models import * 

# Create your models here.
class FeedBack(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    date_feedback = models.DateTimeField(auto_now_add=True)
    feedback = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length=100,null=True, blank=True)
    phoneno = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return f"{self.feedback}"
