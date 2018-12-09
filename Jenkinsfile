node('docker') {
    stage('Checkout') {
        checkout scm
    }
    stage('UnitTest') {
        docker.image('python:3-alpine').inside {
            sh 'pip install -r requirements-dev.txt'
            sh 'py.test'
        }
    }
}
