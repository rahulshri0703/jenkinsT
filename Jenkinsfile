// save global credential as aws-cred in Dashboard > Manage Jenkins> Credentials >System>Global credentials (unrestricted)  


pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {

               withCredentials([[$class: 'UsernamePasswordMultiBinding', 
                                credentialsId: 'awsCred',
                                 usernameVariable: 'AWS_ACCESS_KEY_ID',
                                  passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) 
                                        {
                                
                                            sh "aws s3 ls"
                                            
                                        }
            }
        }
    }
}
