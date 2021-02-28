FROM python:3.5

ENV LD_LIBRARY_PATH=/usr/lib64/

COPY requeriments.txt /etc/
RUN pip install --no-cache-dir -r /etc/requeriments.txt

COPY main.py /apps/main.py
WORKDIR /apps

VOLUME /apps
EXPOSE 8080
CMD ["python3", "/apps/main.py"]
