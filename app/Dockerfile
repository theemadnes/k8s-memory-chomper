FROM python:3.7.4-alpine3.10

#COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app

#RUN pip install -r requirements.txt

RUN addgroup -S appuser && adduser -S -G appuser appuser
USER appuser

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]