 pipeline {
        agent any
        
        stages {
            stage('Start') {
                steps {
                   sh 'pwd'
                   sh 'ls'
                   sh 'docker run -p 8089:8089 -v $PWD:/slack-jenkins locustio/locust -f /slack-jenkins/locustfile.py --headless --only-summary -u 100 -t 30s -r 5 --html /slack-jenkins/$report$(date +%Y%m%d).html'
                }        
                
            }
        }
 }
