FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip
RUN mkdir /app
WORKDIR /app
COPY . /app
EXPOSE 8000
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python3 manage.py makemigrations && python3 manage.py migrate
# RUN python3 manage.py collectstatic --noinput \
#     --username=admin --email=krunalakbari233@gmial.com  --password=admin
# RUN python manage.py shell --noinput < scrip.py
CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]
