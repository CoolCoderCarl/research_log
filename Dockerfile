FROM python:3.9.5

COPY WebInterface.py /
COPY templates/ /templates
COPY requirements.txt requirements.txt

RUN pip3.7 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "./WebInterface.py" ]
