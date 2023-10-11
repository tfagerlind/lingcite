FROM python:3.11.6-alpine3.18

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN python3 -m build
RUN pip install --no-cache-dir --editable .
