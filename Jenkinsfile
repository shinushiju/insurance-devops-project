pipeline {

    agent any

    stages {

        stage('Git Clone') {
            steps {
	         git branch: 'main',
                 credentialsId: 'github-pat',
                 url: 'https://github.com/shinushiju/insurance-devops-project.git'
            }
        }
        
       stage('Install Dependencies') {
 	   steps {
        	sh '''
        	python3 -m venv venv
        	. venv/bin/activate
        	pip install --upgrade pip
        	pip install -r app/requirements.txt
        	'''
    	  }
       }


        stage('Train Model') {
            steps {
                sh './venv/bin/python model/train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'sudo docker build -t insurance-app .'
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
