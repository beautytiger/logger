FROM quay.io/bitnami/python:3.6.13-prod

WORKDIR /app
ADD app.py /app/app.py
RUN chmod a+x /app/app.py

CMD ./app.py
