pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'otodom-tests'
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
                    bat 'docker build -t %DOCKER_IMAGE% .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def workspace = pwd().replace('\\', '/')
                    bat "docker run --rm -v ${workspace}/${ALLURE_RESULTS_DIR}:/app/${ALLURE_RESULTS_DIR} %DOCKER_IMAGE% pytest --alluredir=/app/${ALLURE_RESULTS_DIR}"
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                    def workspace = pwd().replace('\\', '/')
                    bat "docker run --rm -v ${workspace}/${ALLURE_RESULTS_DIR}:/app/${ALLURE_RESULTS_DIR} -v ${workspace}/${ALLURE_REPORT_DIR}:/app/${ALLURE_REPORT_DIR} %DOCKER_IMAGE% allure generate /app/${ALLURE_RESULTS_DIR} -o /app/${ALLURE_REPORT_DIR} --clean"
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