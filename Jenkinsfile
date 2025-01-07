pipeline{

    agent any
    stages {
        stage("checking") {
            steps {
                sh "ls"
            }
        post {
            success {
                sh "echo successfull 100"
                echo "30000"
            }
        }
        }
    }




}