FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

#RUN apk update && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install pipenv && pip install -r requirements.txt

COPY ./ ./

COPY django-entrypoint.sh /django-entrypoint.sh
RUN chmod a+x /django-entrypoint.sh
ENTRYPOINT [ "/django-entrypoint.sh" ]
CMD ["python3", "manage.py" , "runserver", "0.0.0.0:8000"]

