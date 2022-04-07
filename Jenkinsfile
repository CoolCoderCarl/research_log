pipeline {
    agent {
        docker { image 'python:3.7.9' }
    }
    

    stages {
        stage('Build') {
            steps {
                sh 'hello'
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
