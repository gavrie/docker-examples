pipeline {
    agent {
        docker { 
            image 'node:16.13.1-alpine' 
            label '!slaves'
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