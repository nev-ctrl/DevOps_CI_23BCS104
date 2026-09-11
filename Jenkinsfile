pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '=== Stage 1: Checking out code from GitHub for 23BCS104 ==='
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '=== Stage 2: Compiling Python Source Code ==='
                bat 'python -m compileall src/'
            }
        }

        stage('Test') {
            steps {
                echo '=== Stage 3: Executing Automated Unit Tests ==='
                bat 'python -m unittest discover -s tests'
            }
        }

        stage('Result') {
            steps {
                echo '=== Stage 4: CI Pipeline Built & Tested Successfully for 23BCS104 ==='
            }
        }
    }

    post {
        always {
            echo 'CI Pipeline run completed.'
        }
        success {
            echo 'Build and Unit Tests Passed!'
        }
        failure {
            echo 'Build or Unit Tests Failed!'
        }
    }
}
