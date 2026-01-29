FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7000", "app:app"]
