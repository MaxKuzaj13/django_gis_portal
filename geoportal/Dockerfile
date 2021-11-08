FROM python:3.8
WORKDIR /django_gis
COPY requirements.txt /django_gis
# On Linux
# RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
RUN pip install -r requirements.txt
COPY . /django_gis
COPY .env /django_gis