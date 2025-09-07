FROM python:3.10.18-alpine3.22

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ADD . /app

WORKDIR /app

ENTRYPOINT [ "python" ]

CMD ["app.py"]