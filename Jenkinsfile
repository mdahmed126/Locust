 pipeline {
        agent any
        
        stages {
            stage('Start') {
                steps {

                   sh 'docker run -p 8089:8089 -v $PWD:. locustio/locust -f .locustfile.py --headless --only-summary -u 100 -t 30s -r 5 --html ./$report$(date +%Y%m%d).html'
                }        
                
            }
        }
 }
