pipeline{

    agent any

      environment {
    docker_cred = credentials('dockerCred')
    
    }

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

    // stage('BUILDING DOCKER IMAGE') {
    //         steps {
    //             sh "ls"
    //             sh "docker build -t rahulshri0703/mysummer_3000:$BUILD_NUMBER -t rahulshri0703/mysummer_3000:latest ."
    //             // sh "docker tag new999:$BUILD_NUMBER rahulshri0703/new999:$BUILD_NUMBER"
    //         }
        
    //     }

    //     stage('Login to DOCKER') {
    //         steps {
    //             // login to docker
    //             sh "echo $docker_cred_PSW | docker login --username $docker_cred_USR --password-stdin"
    //               // or 
    //              // sh "docker login -u $docker_cred_USR -p $docker_cred_PSW"
    //              // sh "cat ~/my_password.txt | docker login --username foo --password-stdin"
    //              // sh"docker login --username foo --password-stdin < ~/my_password.txt"
                 
    //             // push 
    //             sh "docker push rahulshri0703/mysummer_3000:$BUILD_NUMBER"
    //             sh "docker push rahulshri0703/mysummer_3000:latest"
    //             //delete the images
    //             sh " docker rmi rahulshri0703/mysummer_3000:$BUILD_NUMBER"
    //             sh " docker rmi rahulshri0703/mysummer_3000:latest"
    //         }
    //     }

        stage("docker-login2") {
            steps {
             withCredentials([usernamePassword(credentialsId: 'dockerCred', passwordVariable: 'DOCKER_REGISTRY_PWD', usernameVariable: 'DOCKER_REGISTRY_USER')]) {
                sh "docker login -u ${DOCKER_REGISTRY_USER} -p ${DOCKER_REGISTRY_PWD}"
                sh "echo success9999"

             }
        }
        }

    




    }




}