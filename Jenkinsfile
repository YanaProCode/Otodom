pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.10.6'
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
                python -m venv venv
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