ARG PYTHON_VERSION=3.9.10

FROM python:${PYTHON_VERSION}


RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-contrib \
		postgresql-client \
        python3-pip \
        python3-venv \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /cloud
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install pytest-django
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]