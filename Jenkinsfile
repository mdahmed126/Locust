def call(Map config = [:]) {
    pipeline {
        agent any

        tools {
            nodejs "NodeJs"
        }

        environment {
            RELEASE = "${env.BRANCH_NAME == "develop" || env.BRANCH_NAME == "master"}"
            DEPLOY_TO = "${env.BRANCH_NAME == "develop" ? "staging" : env.BRANCH_NAME == "main" ? "production" : ""}"
        }

            stage('Build') {
                steps {
                    sh 'npm ci'
                }
            }

            stage('Test') {
                steps {
                    sh 'npm run test'
                }
            }

           }

            stage('Deploy') {

                when { expression { env.RELEASE == "true" } }

                parallel {

                    stage("staging") {
                        when { expression { env.DEPLOY_TO == "staging" } }
                        steps {
                            copyArtifacts(projectName: 'Locust//dev', filter: '**/*.html')
                            script {
                                if (config.build) {
                                    stage ('npm build') {
                                        sh 'npm run build'
                                    }
                                }
                            }
                            sh 'ls -ltr'
                            sh 'npm run deploy-staging'
                        }
                    }

                    stage("production") {
                        when { expression { env.DEPLOY_TO == "production" } }
                        steps {
                            copyArtifacts(projectName: 'Locust/main', filter: '**/*.html')
                            script {
                                if (config.build) {
                                    stage ('npm build') {
                                        sh 'npm run build'
                                    }
                                }
                            }
                            sh 'ls -ltr'
                            sh 'npm run deploy-production'
                        }
                    }

                }

            }

        }

        post {

            always {

                sh 'npm run generate-report'

                ppublishHTML target: [
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
        
    
