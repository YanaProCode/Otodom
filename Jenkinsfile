pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-u root'
        }
    }
    environment {
        ALLURE_RESULTS_DIR = 'allure-results'
        ALLURE_REPORT_DIR = 'allure-report'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('otodom-tests')
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.image('otodom-tests').inside {
                        sh 'pytest --alluredir=${ALLURE_RESULTS_DIR}'
                    }
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                    docker.image('otodom-tests').inside {
                        sh 'allure generate ${ALLURE_RESULTS_DIR} -o ${ALLURE_REPORT_DIR} --clean'
                    }
                }
            }
        }
        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: "${ALLURE_RESULTS_DIR}"]]
                ])
            }
        }
    }
}