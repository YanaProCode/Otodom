pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.10.6'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YanaProCode/Otodom.git'
            }
        }
        stage('Setup') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
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