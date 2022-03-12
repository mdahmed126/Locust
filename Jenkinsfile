pipeline {
        agent any
        
        stages {
            stage('Start') {
             steps {
                    sh 'python3 -m venv venv/'
                    sh 'pip3 install -r requirements.txt'
                    sh 'ls'
                    sh '''locust -f locustfile.py --headless --only-summary -u 100 -t 10s -r 5 --html $report$(date +%Y%m%d).html'''
             }
                
            }
        }
 }
