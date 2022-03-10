 pipeline {
        agent any
        
        stages {
            stage('Start') {
                steps {
                   sh 'docker run -p 8089:8089 -v /vol/jenkins_home/workspace/slack-jenkins:/Locust locustio/locust -f /Locust/locustfile.py --headless --only-summary -u 100 -t 10s -r 5 --html /mnt/locust/new1223.html'
                }
                
            }
        }
 }
