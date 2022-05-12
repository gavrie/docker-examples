pipeline {
    agent {
        docker { 
            image 'python:3.10.4-slim-bullseye'
            label 'docker'
        }
    }

    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    }
}