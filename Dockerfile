FROM python:3.8

WORKDIR /usr/src/parking
COPY requirements.txt /usr/src/parking
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .
