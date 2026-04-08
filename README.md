🚀 DevOps Project: Docker + Jenkins CI Pipeline

📌 Project Overview

This project demonstrates a complete DevOps workflow using Docker and Jenkins to automate the build, execution, and testing of a simple Python application.

The application (sum.py) takes two numbers as input and returns their sum. The entire process is automated using a Jenkins pipeline.

⸻

⚙️ Technologies Used
	•	🐳 Docker
	•	🔧 Jenkins
	•	🐍 Python
	•	💻 Shell scripting

⸻

📂 Project Structure.
├── Dockerfile
├── Jenkinsfile
├── sum.py
├── test_variables.txt
└── README.md🐳 Docker Setupdocker build -t sum-app .Run Containerdocker run -dit sum-appExecute Python Scriptdocker exec <container_id> python /app/sum.py 5 10🔁 Jenkins Pipeline

The Jenkins pipeline automates the following steps:
	1.	Build Stage
	•	Builds Docker image (sum-app)
	2.	Run Stage
	•	Runs container from the image
	3.	Test Stage
	•	Executes Python script inside container
	•	Validates output
	4.	Post Actions
	•	Stops and removes container

⸻

📜 Jenkinsfile (Pipeline)pipeline {
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
}🧪 Example OutputInput: 5 10  
Output: 15🎯 Key Learnings
	•	Automated CI pipeline using Jenkins
	•	Docker containerization and execution
	•	Handling permissions and environment issues
	•	Debugging real-world DevOps problems

⸻

🚀 Future Improvements
	•	Add unit testing framework
	•	Integrate GitHub Webhooks for auto-trigger
	•	Deploy application using Kubernetes

⸻

👩‍💻 Author

Nishi Macwan
