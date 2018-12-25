FROM yoanlin/opencv-python3

ADD . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uwsgi","--ini","/app/uwsgi.ini"]
# CMD python application.py