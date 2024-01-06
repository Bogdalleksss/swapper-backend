# Sets the base image for subsequent instructions
FROM python:3.8-slim-buster
# Sets the working directory in the container
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD ["flask", "run", "--port", "8000", "--host=0.0.0.0"]