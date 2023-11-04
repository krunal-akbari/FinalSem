from home.models import Customer
from django.contrib.auth.models import User
user = User.objects.all().filter(is_superuser=True).last()
c = Customer(user=user)
c.save()
exit()
