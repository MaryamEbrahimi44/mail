
FROM ubuntu:lunar-20230816

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
RUN pip install celery
RUN pip install fastapi
RUN pip install sqlalchemy-orm

WORKDIR /mail

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]