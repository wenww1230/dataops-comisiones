pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t dataops-comisiones .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'mkdir -p output'
                sh 'docker run --rm -v "$WORKSPACE/output:/app/output" dataops-comisiones'
            }
        }

        stage('Check Output') {
            steps {
                sh 'ls -lh output'
            }
        }
    }
}
