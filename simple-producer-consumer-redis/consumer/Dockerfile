FROM python:3.8.13

WORKDIR /src
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 5011

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5011", "app:app"]