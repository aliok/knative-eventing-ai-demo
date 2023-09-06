FROM python:3.9

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app

RUN pip install -r requirements.txt

COPY . /opt/app

EXPOSE 5000
ENV IMG_MAX_WIDTH=640
ENV IMG_MAX_HEIGHT=640

CMD ["flask", "--app", "main", "run", "--host", "0.0.0.0"]

