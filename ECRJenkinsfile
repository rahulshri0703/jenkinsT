def COLOR_MAP = [
    'SUCCESS': 'good',
    'FAILURE': 'danger',
]

pipeline {
    
    agent any

      environment {

        appRegistry = "060795944326.dkr.ecr.us-east-1.amazonaws.com/myrepo33"
        vprofileRegistry ="http://060795944326.dkr.ecr.us-east-1.amazonaws.com"
        registryCredential = "ecr:us-east-1:awsPluginCred"
        // awsPluginCred is AWS credential using Manage>Jenkins>Credentials>System>Global credentials (unrestricted)>AWS credential
        // registryCredential = 'ecrPass'  
        //  create a cred in Dashboard : Manage>Jenkins>Credentials>System>Global credentials (unrestricted)

        // username = AWS
        // password = get password using: aws ecr get-login-password
        //
    }

     stages {
 


        //   stage('BUILDING DOCKER IMAGE') {
        //     steps {
        //         sh "ls"
        //         sh "docker build -t $appRegistry:$BUILD_NUMBER -t $appRegistry:latest ."
        //         // sh "docker tag new999:$BUILD_NUMBER rahulshri0703/new999:$BUILD_NUMBER"
        //     }
        
        // }

        // create a docker_credentials in Dashboard>Manage Jenkins>Credentials>System>Global credentials (unrestricted)

        //     stage("login to AWS") {
        //     steps {
        //           withCredentials([[$class: 'UsernamePasswordMultiBinding', 
        //                         credentialsId: 'awsCred',
        //                          usernameVariable: 'AWS_ACCESS_KEY_ID',
        //                           passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) 
        //                                 {
                                
        //                                     sh "aws s3 ls"
                                            
        //                                 }
        //     }
        // }
        
        // stage('Login to DOCKER') {
        //     steps {

        //          withCredentials([[$class: 'UsernamePasswordMultiBinding', 
        //                         credentialsId: 'awsCred',
        //                          usernameVariable: 'AWS_ACCESS_KEY_ID',
        //                           passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) 
                
        //         {
        //         // login to docker
        //          sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $appRegistry"
        //         // push 
        //         sh "docker push $appRegistry:$BUILD_NUMBER"
        //         sh "docker push $appRegistry:latest"
        //         //delete the images
        //         // sh " docker rmi rahulshri0703/dummy_3000:$BUILD_NUMBER"
        //         // sh " docker rmi rahulshri0703/dummy_3000:latest"
        //     }
        //     }
        // }


        stage('Build App Image') {
            // agent { label 'KOPS' }
       steps {
       
         script {
                dockerImage = docker.build( appRegistry + ":$BUILD_NUMBER", ".")
             }

     }
    
    }


         stage('Upload App Image') {
            // agent { label 'KOPS' }
          steps{
            script {
              docker.withRegistry( vprofileRegistry, registryCredential ) {
                dockerImage.push("$BUILD_NUMBER")
                dockerImage.push('latest')
              }
            }
          }
     }



     }

   post {
        always {
            echo "slack notification"
            slackSend channel: '#jenkinstrial', // channel name
                color: COLOR_MAP[currentBuild.currentResult],
                message: "*${currentBuild.currentResult}:* Job ${env.JOB_NAME} build ${env.BUILD_NUMBER} \n More info at ${env.BUILD_URL}"

        }
    }

}