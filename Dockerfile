FROM python:3.9.16

WORKDIR /usr/src/application
#copy requirements.txt in container
RUN apt update && apt-get install -y nmap && apt-get install -y libcurl4-openssl-dev libssl-dev
COPY requirements.txt ./
#install requirements in container
RUN pip install --no-cache-dir -r requirements.txt
#copy contents entire contents in WORKDIR folder
COPY . . 
#this cmd will be overwritten from docker-compose.yaml file command
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]