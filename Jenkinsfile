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
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest --browser=chromium --tool=playwright
                '''
            }
        }
    }

    post {
        always {
            junit 'reports/*.xml'
        }
    }
}