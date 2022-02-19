FROM python:3.10

RUN python -m pip install --upgrade pip

COPY requirements.txt /src/
RUN pip3 install -r /src/requirements.txt

COPY . /src/

WORKDIR /src
ENTRYPOINT [ "/usr/local/bin/python3", "manage.py", "runserver", "0.0.0.0:80" ]

EXPOSE 80