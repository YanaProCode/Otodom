pipeline {
    agent any

    environment {
        CHOCO_PATH = 'C:\\ProgramData\\chocolatey\\bin\\choco.exe'
    }

    stages {
        stage('Install Chocolatey') {
            steps {
                bat '''
                @echo off
                SET "CHOCO_INSTALL=%SystemDrive%\\choco"
                IF NOT EXIST "%CHOCO_INSTALL%" (
                    powershell -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
                )
                '''
            }
        }
        stage('Install Python') {
            steps {
                bat '%CHOCO_PATH% install python --version=3.10.6 -y'
            }
        }
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
                pip install pytest selenium playwright pytest-playwright
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