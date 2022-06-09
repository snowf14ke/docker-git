FROM python:3.9

WORKDIR /

COPY . .

#installing required libraries
RUN pip3 install -r requirements.txt


#starting flask app
CMD ["flask", "run", "--host=0.0.0.0"]