FROM python:3.9-slim
WORKDIR  /code

COPY ./requirements.txt ./
RUN pip install -r requirements.txt 



COPY  . . 
ENV PORT=85
EXPOSE  85
CMD [ "python","manage.py","runserver","0.0.0.0:85" ]
