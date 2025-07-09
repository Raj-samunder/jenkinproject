pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning Repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t acronym-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'echo "Sample Input: World Health Organization" | docker run -i acronym-app'
            }
        }
    }
}
