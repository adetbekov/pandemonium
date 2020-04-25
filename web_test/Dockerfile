FROM python

RUN mkdir -p /home/project/web_test
WORKDIR /home/project/web_test
COPY requirements.txt /home/project/web_test
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/web_test