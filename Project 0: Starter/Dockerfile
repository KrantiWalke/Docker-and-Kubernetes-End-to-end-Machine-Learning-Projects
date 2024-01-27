FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ENV FLASK_APP=server.py
COPY . /app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8111"]
