pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\Yana_Proshak\\AppData\\Local\\Programs\\Python\\Python310\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YanaProCode/Otodom.git'
            }
        }
        stage('Setup') {
            steps {
                bat '''
                %PYTHON_PATH% -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                pip install allure-pytest
                '''
            }
        }
        stage('Install Playwright Browsers') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                playwright install
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest --test-browser=chromium --test-tool=playwright --alluredir=allure-results
                '''
            }
        }
        stage('Generate Allure Report') {
            steps {
                bat '''
                allure generate allure-results --clean -o allure-report
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}