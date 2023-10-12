pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'pkiran1017'  // Replace with your Docker Hub username
        DOCKER_HUB_PASSWORD = 'Pkiran@101714@'        // Replace with your Docker Hub password
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Build and Push Docker Images') {
            steps {
                script {
                    // Authenticate with Docker Hub
                    sh "docker login -u \$DOCKER_HUB_USERNAME -p \$DOCKER_HUB_PASSWORD"

                    // Build and tag the Docker Compose project
                    sh "docker-compose -f \$DOCKER_COMPOSE_FILE build"

                    // Push Docker images to Docker Hub
                    sh "docker-compose -f \$DOCKER_COMPOSE_FILE push"
                }
            }
        }
    }
}
