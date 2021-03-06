FROM python:3.7-alpine

RUN pip install Django==2.2.1 \
                pytz==2019.1 \
                sqlparse==0.3.0

COPY . /app/
WORKDIR /app/
RUN pip3 install -r ./requirements.txt

ENTRYPOINT ["sh",  "-c", "cd simple_register_django && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

