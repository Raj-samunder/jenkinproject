pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                echo 'Running acronym generator...'
                sh 'echo "World Health Organization" | python3 acronym.py'
            }
        }
    }
}
