pipeline {
    agent docker { image 'python:3.7.9' }

    stages {
        stage('Build') {
            steps {
                sh 'podman build -t docker.io/h0d0user/logger_image_tester:latest .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
