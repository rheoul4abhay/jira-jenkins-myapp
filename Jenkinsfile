pipeline {
    agent {
        label 'docker-node'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building on slave node"
                sh 'python3 app.py'
            }
        }
    }
}
