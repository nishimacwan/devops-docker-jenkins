pipeline {
    agent any

    environment {
        DOCKER = "/usr/local/bin/docker"
        CONTAINER_ID = ""
        TEST_FILE_PATH = "test_variables.txt"
    }

    stages {

        stage('Build') {
            steps {
                sh "$DOCKER build -t sum-app ."
            }
        }

        stage('Run') {
            steps {
                script {
                    env.CONTAINER_ID = sh(
                        script: "$DOCKER run -dit sum-app",
                        returnStdout: true
                    ).trim()
                }
            }
        }

        stage('Test') {
            steps {
                sh "$DOCKER exec $CONTAINER_ID python /app/sum.py 5 10"
            }
        }
    }

    post {
        always {
            script {
                sh "$DOCKER stop $CONTAINER_ID || true"
                sh "$DOCKER rm $CONTAINER_ID || true"
            }
        }
    }
}
