FROM python:3.10-slim

# Установка необходимых пакетов, включая wget и gnupg
RUN apt-get update && apt-get install -y \
    gnome-browser-connector \
    wget \
    gnupg \
    && apt-get clean

# Установка Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Копирование и установка зависимостей Python
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . /app

# Установка Allure
RUN wget -q -O - https://dl.bintray.com/qameta/generic/gpg.key | apt-key add - \
    && sh -c 'echo "deb https://dl.bintray.com/qameta/generic-deb all main" > /etc/apt/sources.list.d/qameta.list' \
    && apt-get update \
    && apt-get install -y allure

# Установка дополнительных зависимостей
RUN pip install webdriver-manager
RUN pip install playwright
RUN playwright install
RUN pip install selenium
RUN pip install pytest pytest-allure-adaptor

# Команда для запуска тестов
CMD ["pytest", "--alluredir=allure-results"]