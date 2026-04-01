pipeline {
    agent any
    triggers {
        scm 'H/1 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                sh 'python backend/app.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover -s backend/tests'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python backend/deploy.py'
            }
        }
    }
    post {
        success {
            echo 'Pipeline executed successfully'
        }
        failure {
            echo 'Pipeline execution failed'
        }
    }
}