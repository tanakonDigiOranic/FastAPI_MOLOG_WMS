FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY libs /app/libs
COPY server.py /app/server.py
COPY requirements.txt /app/requirements.txt

EXPOSE 5000
RUN pip install -U  pip && pip install -r /app/requirements.txt
WORKDIR /app

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "5000"]