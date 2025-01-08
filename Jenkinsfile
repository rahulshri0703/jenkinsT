def COLOR_MAP = [
    'SUCCESS': 'good',
    'FAILURE': 'danger',
]

pipeline {
    
    agent any


     stages {


        stage('A success') {
            // agent { label 'KOPS' }
       steps {
       
         sh "echo 555"

     }
     post {
      success {
        sh " this is a success"
      }
     }
    
    }


     stage('A failure') {
            // agent { label 'KOPS' }
       steps {
       
         sh "echo5 555"

     }
     post {
      failure {
        sh " this is a failure"
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

