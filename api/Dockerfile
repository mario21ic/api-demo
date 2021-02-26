FROM python:3.5

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /apps

COPY src/api.py /apps/api.py
ENV FLASK_APP=api.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8080"]
