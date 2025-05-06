FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    gnome-browser-connector \
    wget \
    && apt-get clean

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable

RUN apt-get update && apt-get install -y firefox

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN wget -q -O - https://dl.bintray.com/qameta/generic/gpg.key | apt-key add - \
    && sh -c 'echo "deb https://dl.bintray.com/qameta/generic-deb all main" > /etc/apt/sources.list.d/qameta.list' \
    && apt-get update \
    && apt-get install -y allure

RUN pip install webdriver-manager
RUN pip install playwright
RUN playwright install
RUN pip install selenium
RUN pip install pytest pytest-allure-adaptor

CMD ["pytest", "--alluredir=allure-results"]