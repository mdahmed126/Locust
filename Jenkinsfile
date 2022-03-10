 pipeline {
        agent any
        
        stages {
            stage('Start') {
                steps {
                   sh 'pwd'
                   sh 'ls'
                   sh 'docker run -p 8089:8089 -v $PWD:/Locust locustio/locust -f /Locust/locustfile.py ls'
                }
                
            }
        }
 }
