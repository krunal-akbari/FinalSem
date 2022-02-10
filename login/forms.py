from django.forms import ModelForm
from . import models

class  CustomerForm(ModelForm):
    class Meta:
        model = models.CustomerModel
        fields = ['cname','password']

