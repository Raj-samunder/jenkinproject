pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning Repository...'
            }
        }

        
        stage('Run Docker Container') {
            steps {
                sh 'echo "Sample Input: World Health Organization" | docker run -i acronym-app'
            }
        }
    }
}
