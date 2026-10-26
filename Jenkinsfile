pipeline{
    agent any
    stages{
        stage('Checkout the scm'){
            steps{
                echo 'Checking out the source code from SCM'
                checkout scm
            }
        }
        stage('Build Docker Image'){
            steps{
                echo 'Building the Docker image'
                bat 'docker build -t myapp:latest .'
            }
        }
        stage('Docker Image push'){
            steps{
                echo 'Pushing the Docker image to Docker Hub...'
                    bat 'docker tag myapp:latest guglothkumari/myapp:latest'
                    bat 'docker push guglothkumari/myapp:latest'
                }
            }
        }
        stage('Run Docker Container'){
            steps{
                echo 'Running the Docker container...'
                bat 'docker run -d -p 5000:5000 myapp:latest'
            }
        }
        
        stage('Running docker container'){
            steps{
                echo 'Running the docker container...'
                bat 'docker run -d -p 5000:5000 guglothkumari/myapp:latest'
            }
        }
    }
    post{
        success{
            echo 'Pipeline completed successfully!'
        }
        failure{
            echo 'Pipeline failed. Please check the jenkins files'
        }
    }
}