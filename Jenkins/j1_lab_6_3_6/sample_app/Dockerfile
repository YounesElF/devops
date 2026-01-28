FROM python:3.11-slim

WORKDIR /home/sample_app

# pip “thread/progress” issues vermijden (zoals je eerder had)
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_PROGRESS_BAR=off \
    APP_VERSION="1.0"

RUN pip install --upgrade pip && pip install flask

COPY ./static /home/sample_app/static
COPY ./templates /home/sample_app/templates
COPY sample_app.py /home/sample_app/

EXPOSE 5555
CMD ["python", "sample_app.py"]
