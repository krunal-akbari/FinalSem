FROM continuumio/miniconda3 AS base

RUN mkdir app
WORKDIR app
COPY requirements.txt requirements.txt
RUN apt update -y && apt upgrade -y && apt install gcc -y && pip install django django-admin

RUN pip install -r requirements.txt  

FROM base AS installation
COPY . .
EXPOSE 8000
CMD [  "python", "./manage.py", "runserver", "0.0.0.0:8000" ]