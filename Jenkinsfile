pipeline {
        agent any
        
        stages {
             steps {
                    sh 'mkdir -p locust_results' 
                    sh 'python3 -m venv venv/'
                    sh 'pip3 install -r requirements.txt'
                    sh 'ls'
                    sh '''locust -f locustfile.py --headless --only-summary -u 100 -t 10s -r 5 --html $report$(date +%Y%m%d%H%M).html'''
                    sh 'cp -r /var/jenkins_home/workspace/Locust/*.html  locust_results' 
             }
             stage('Start') {   
             step ([$class: 'CopyArtifact',
                  projectName: ‘Locust’,
                   filter: 'locust_results/*']);
       
              post {
                always {
                     sh 'npm run generate-report'

                publishHTML target: [
                     allowMissing: false,
                      alwaysLinkToLastBuild: true,
                      keepAll: true,
                      reportDir: 'locust_results',
                      reportFiles: 'index.html',
                      reportName: 'Locust-Report',
                      includes: 'index.html'
               ]        
          }
        }
 }
        }
}    
