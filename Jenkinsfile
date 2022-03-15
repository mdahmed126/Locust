pipeline {
        agent any
        
        stages {
            stage('Start') {
             steps {
                    sh 'python3 -m venv venv/'
                    sh 'pip3 install -r requirements.txt'
                    sh 'ls'
                    sh '''locust -f locustfile.py --headless --only-summary -u 100 -t 10s -r 5 --html index.html'''
             }
        post {
        always {

                publishHTML([allowMissing: false,
                      alwaysLinkToLastBuild: true,
                      keepAll: true,
                      reportDir: 'locust_results',
                      reportFiles: 'index.html',
                      reportName: 'Locust-Report',
                      includes: 'index.html'
     ])        
            }
        }
 }
        }
}
