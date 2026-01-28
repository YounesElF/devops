FROM python:3.11-slim

WORKDIR /app

# pip fixes voor jouw omgeving (geen progress threads)
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_PROGRESS_BAR=off

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app/app.py .

# SQLite db komt hier
RUN mkdir -p /data
ENV DB_PATH=/data/notes.db

EXPOSE 5050
CMD ["python", "app.py"]

