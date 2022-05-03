FROM python:3.9 AS builder

WORKDIR /build
COPY requirements.txt /build/requirements.txt
RUN pip3.9 install --user -r requirements.txt



FROM python:3.9

WORKDIR /webapp

COPY webapp.py /webapp
COPY templates/ /webapp/templates
COPY --from=builder /root/.local /root/.local

VOLUME /var/log/research_logs /webapp/research_logs

CMD [ "python3.9 ./webapp.py" ]