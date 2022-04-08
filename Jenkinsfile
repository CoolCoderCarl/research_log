pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t h0d0user/flask_web_test:latest .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p 5000:5000 h0d0user/flask_web_test:latest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'docker push h0d0user/flask_web_test:latest'
            }
        }   
    }
    
    post {
        success {
            echo '${env.JENKINS_URL}'
            }
    }         
}
