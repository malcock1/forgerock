FROM python:3

WORKDIR .

COPY requirements.txt ./
COPY webserver.py ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python", "-u", "./webserver.py" ]