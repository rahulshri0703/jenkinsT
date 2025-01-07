FROM python:3.10-slim-buster

WORKDIR /app

COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt

COPY . .

CMD [ "python3","-m","gunicorn","--bind","0.0.0.0:3000","api:app" ]