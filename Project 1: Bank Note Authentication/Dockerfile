# Using an updated Anaconda image
FROM continuumio/anaconda3:2022.05
COPY . /usr/app/
# Install build essentials
RUN apt-get update && apt-get install -y \
    build-essential
EXPOSE 5000
WORKDIR /usr/app/
# Upgrade pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python flask_api.py