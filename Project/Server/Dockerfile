# syntax=docker/dockerfile:1

FROM python:3.9.10

WORKDIR .

#RUN apt update && apt install libmysqlclient-dev
COPY requirements.txt requirements.txt 
#RUN  python -m pip install --upgrade pip && pip3 install -r requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=80"]
