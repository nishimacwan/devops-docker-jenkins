# DevOps Project: Docker + Jenkins CI Pipeline

A small project to practise a complete DevOps workflow: Jenkins automatically builds, runs and tests a Dockerised Python app.

The app (`sum.py`) takes two numbers and returns their sum.

## Technologies
Docker · Jenkins · Python · Shell scripting

## Project structure
```
├── Dockerfile
├── Jenkinsfile
├── sum.py
├── test_variables.txt
└── README.md
```

## Run it with Docker
```bash
docker build -t sum-app .
docker run -dit sum-app
docker exec <container_id> python /app/sum.py 5 10
```

## The Jenkins pipeline
See the `Jenkinsfile`. It runs 4 steps:
1. **Build**: builds the Docker image `sum-app`
2. **Run**: starts a container from the image
3. **Test**: runs the script inside the container and checks the output (5 + 10 = 15)
4. **Clean up**: always stops and removes the container, even if a step fails

## What I learned
- Automating a CI pipeline with Jenkins
- Building and running Docker containers
- Fixing permission and environment issues between Jenkins and Docker

## Next steps
- Add unit tests with pytest
- Trigger the pipeline automatically with a GitHub webhook
- Deploy with Kubernetes
