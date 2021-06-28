FROM python:3.7

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install python3-dev build-essential  gcc  -y

WORKDIR /app

# Install python3 lib
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8401
#CMD ["python3"]
CMD ["uvicorn","--host","0.0.0.0","--workers","2","--port","8502","--reload","main:app"]