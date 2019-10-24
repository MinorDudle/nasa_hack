FROM tensorflow/tensorflow:latest-py3

RUN apt-get update \
 && apt-get install -y libsm6 libxext6 libxrender-dev supervisor\
 && mkdir -p /var/log/supervisor \
 && mkdir -p /etc/supervisor/conf.d \
 && pip install --upgrade pip\
 && pip install Flask==1.0.3 Jinja2==2.10 json-merge-patch==0.2 \
  jsonschema==3.0.1 Keras==2.3.1 numpy==1.16.3 pandas==0.24.2 \
  Pillow==6.2.0 requests==2.21.0 scipy==1.2.2 tensorboard==2.0.0 \
  tensorflow-hub==0.6.0 urllib3==1.24.2 opencv-python openpyxl xlrd

USER root

COPY . ./app

WORKDIR /app

CMD ["supervisord", "-c", "./supervisord.conf"]