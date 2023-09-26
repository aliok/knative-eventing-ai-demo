FROM python:3.9

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app

RUN pip install -r requirements.txt

COPY . /opt/app

EXPOSE 5000

# 1MiB
ENV MAX_IMG_SIZE_IN_BYTES=1000000
ENV MAX_IMG_WIDTH=640
ENV MAX_IMG_HEIGHT=640

ENV S3_BUCKET_NAME='ai-demo'
ENV S3_ACCESS_SSL_VERIFY='true'

CMD ["flask", "--app", "main", "run", "--host", "0.0.0.0"]

