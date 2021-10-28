FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /code

COPY libs /app/libs
COPY ./.env /code/.env
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]