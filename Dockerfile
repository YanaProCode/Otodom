FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    gnome-browser-connector \
    wget \
    gnupg \
    && apt-get clean

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN wget -q -O /tmp/allure-2.34.0.tgz https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.34.0/allure-commandline-2.34.0.tgz \
    && tar -zxvf /tmp/allure-2.34.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.34.0/bin/allure /usr/bin/allure

RUN pip install webdriver-manager
RUN pip install playwright
RUN playwright install
RUN pip install selenium
RUN pip install pytest pytest-allure-adaptor

RUN sed -i 's/collections.Mapping/collections.abc.Mapping/' /usr/local/lib/python3.10/site-packages/namedlist.py
RUN sed -i 's/collections.Sequence/collections.abc.Sequence/' /usr/local/lib/python3.10/site-packages/namedlist.py

RUN echo "[pytest]\naddopts = --alluredir=/app/allure-results" > /app/pytest.ini

CMD ["pytest", "--alluredir=allure-results"]