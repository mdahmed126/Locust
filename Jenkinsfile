pipeline {
        agent any
        
        stages {
            stage('Start') {
             steps {
                    sh 'python3 -m venv venv/ '
                    sh 'source venv/bin/activate'
                    sh 'pip3 install -r requirements.txt'
                    sh 'ls'
                    sh '''locust -f locustfile.py'''
             }
                
            }
        }
 }
