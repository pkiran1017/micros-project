pipeline {
    agent any
    stages {
        stage('Build and Dockerize') {
            steps {
                sh 'sudo docker-compose build'
            }
        }
        stage('Deploy to Docker') {
            steps {
                sh 'sudo docker-compose up -d'
            }
        }
    }
    post {
        always {
            sh 'sudo docker-compose down'
        }
    }
}
