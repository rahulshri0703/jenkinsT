def COLOR_MAP = [
    'SUCCESS': 'good',
    'FAILURE': 'danger',
]
// valid conditions are [always, changed, fixed, regression, aborted, success, unsuccessful, unstable, failure, notBuilt, cleanup]
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

      always {
        sh "666"
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
        sh "echo  'this is a failure'"
      }
       unsuccessful {
        sh " echo 'this is a unsuccessful'"
      }
       aborted {
        sh " echo 'abort'"
      }
        always {
        sh "77"
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

