pipeline {

    agent any

    stages {

        stage('Git Clone') {
            steps {
                git 'https://github.com/shinushiju/insurance-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r app/requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 model/train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t insurance-app .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker tag insurance-app shinushiju/insurance-app:latest
                docker push shinushiju/insurance-app:latest
                '''
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
