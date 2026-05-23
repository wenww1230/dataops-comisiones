pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                checkout scm
            }
        }

        stage('Construir imagen Docker') {
            steps {
                sh 'docker build -t dataops-comisiones .'
            }
        }

        stage('Ejecutar contenedor') {
            steps {
                sh 'mkdir -p output'
                sh 'docker run --rm -v $WORKSPACE/output:/app/output dataops-comisiones'
            }
        }

        stage('Verificar artefacto') {
            steps {
                sh 'ls -lh output'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente. El archivo Excel fue generado.'
        }

        failure {
            echo 'El pipeline falló. Revisar logs.'
        }
    }
}
