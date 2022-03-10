 pipeline {
        agent any
        
        stages {
            stage('Start') {
                steps {
                   sh 'mkdir -p tmp'
                   sh 'docker run -p 8089:8089 -v /vol/jenkins_home/workspace/slack-jenkins:/Locust -v /tmp:/tmp locustio/locust -f /Locust/locustfile.py --headless --only-summary -u 100 -t 10s -r 5 --html /tmp/$report$(date +%Y%m%d)_LOCUST.html'         
                   sh 'ls'
                   sh 'docker cp /tmp/$report$(date +%Y%m%d)_LOCUST.html 8f7e240590f2:/$report$(date +%Y%m%d)_LOCUST.html'
                 sh 'cd /'
                 sh 'ls'
                 sh 'pwd'
                }
                
            }
        }
 }
