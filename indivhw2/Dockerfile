FROM python:3.8-alpine
WORKDIR /home/data 
ADD docker.py /
# RUN pip install pystrich
COPY . .
CMD [ "python", "./docker.py" ]