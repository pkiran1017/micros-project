pipeline {
    agent any
    stages {
        stage('Build and Dockerize') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Deploy to Docker') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
    post {
        always {
            sh 'docker-compose down'
        }
    }
}
