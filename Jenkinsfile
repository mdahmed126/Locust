 pipeline {
        agent any
        
        stages {
            stage('Start') {
                steps {
                   sh 'pwd'
                   sh 'ls'
                   sh 'docker run busybox'
                   sh 'docker run -p 8089:8089 -v $PWD:/mnt/locust --privileged locustio/locust -f /mnt/locust/locustfile.py ls'
                }
                
            }
        }
 }
