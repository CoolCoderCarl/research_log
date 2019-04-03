FROM python:3.7.2

COPY WebInterface.py /
COPY templates/ /templates

#add silence 
RUN pip install -y Flask
RUN pip install -y wtforms
RUN pip install -y click

ENTRYPOINT [ "python" ]

CMD [ "./WebInterface.py" ]
