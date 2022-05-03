FROM python:3.9 AS builder

WORKDIR /build

COPY webapp.py /build
COPY templates/ /build/templates
COPY requirements.txt /build/requirements.txt

RUN pip3.9 install -r requirements.txt



FROM python:3.9

WORKDIR /webapp

VOLUME /var/log/research_logs /webapp/research_logs

COPY --from=builder /build /webapp

CMD [ "python3.9 /webapp.py" ]