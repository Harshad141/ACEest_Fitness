pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-flask-app .'
            }
        }
        stage('Run Tests') {
    steps {
        sh '''
        docker run --rm aceest-flask-app /bin/bash -c "
            source venv/bin/activate &&
            pytest --cov=app --cov-report=xml
        "
        '''
    }
}
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh 'sonar-scanner'
                }
            }
        }
    }
}
