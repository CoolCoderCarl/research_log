FROM python:3


ADD WebInterface.py /
ADD templates/ /templates

RUN pip install Flask
RUN pip install wtforms

CMD [ "python" , "./WebInterface.py" ]
