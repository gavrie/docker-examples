pipeline {
    agent {
        docker { 
            image 'node:16.13.1-alpine' 
            label 'docker'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}