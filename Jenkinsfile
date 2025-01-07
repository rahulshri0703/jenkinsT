// save global credential as aws-cred in Dashboard > Manage Jenkins> Credentials >System>Global credentials (unrestricted)  


pipeline {
    agent any

    stages {

        // stage('Hello') {
        //     steps {

        //        withCredentials([[$class: 'UsernamePasswordMultiBinding', 
        //                         credentialsId: 'awsCred',
        //                          usernameVariable: 'AWS_ACCESS_KEY_ID',
        //                           passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) 
        //                                 {
                                
        //                                     sh "aws s3 ls"
                                            
        //                                 }
        //     }
        // }

    // stage('test aws') {
    //       steps {
    //     withAWS(credentials: 'awsPluginCred', region: 'us-east-1') {
    //       sh 'aws s3 ls'
    //       sh "echo 3672"
    //     }
    //   }
    //  }

    stage("aws-login2") {
            steps {
             withCredentials([usernamePassword(credentialsId: 'awsCred', 
                                    passwordVariable: 'AWS_ACCESS_KEY_ID', 
                                    usernameVariable: 'AWS_SECRET_ACCESS_KEY')]) {


                                          sh "aws s3 ls"
                                          sh "echo 9980"
                                        
                                    }
            }
    }





    }
}
