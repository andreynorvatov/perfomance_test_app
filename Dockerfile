FROM python:3.10.1-slim
# LABEL maintainer="p_app"

# VOLUME /var/lib/django-db

# ENV DATABASE_URL sqlite:////var/lib/django-db/db.sqlite

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

#RUN pip install --no-cache-dir uwsgi==2.0.20
ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /srv
ADD perfomance_test_app/ /srv

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#RUN ./manage.py collectstatic

#CMD uwsgi --htp :8000 --wsgi-file app/wsgi.py --master --process 4 --threads 2