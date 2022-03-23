# Final Sem
persoal university project it will change afterword's
### Installation
python [python.org](htttp://www.python.org)
pip install django
pip install -U django-jazzmin
pip install django-paypal
### Run project
git clone https://github.com/AKrunal/FinalSem.git
>runnig code
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
this will ask you to give some credentials
```
username : <username will be here>
email : <email id if you want>
password : <your password>
conform password : <same password as above>
```
after that will add customer as same but need some more might be some bug
```
python3 manage.py shell 
from home.models import Customer
from django.contrib.auth.models import User
user = User.objects.all().filter(is_superuser=True).last()
c = Customer(user=user)
c.save()
exit()
```
just copy past that  code and it will setting up created


# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| 2.0.x   | :x:                |
| 3.0.x   | :x:                |
| > 4.0   | :white_check_mark: |

## Reporting a Vulnerability

Use this section to tell people how to report a vulnerability.

Tell them where to go, how often they can expect to get an update on a
reported vulnerability, what to expect if the vulnerability is accepted or
declined, etc.

