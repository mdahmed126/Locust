 pipeline {
        agent any
        
        stages {
            stage('Start') {
                steps {
                   sh 'pwd'
                   sh 'ls'
                   sh 'docker run -p 8089:8089 -v $PWD:/Locust locustio/locust -f /Locust/locustfile.py --headless --only-summary -u 100 -t 30s -r 5 --html /Locust/$report$(date +%Y%m%d).html'
                }        
                
            }
        }
 }
