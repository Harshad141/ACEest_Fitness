# 🏋️ ACEest Fitness & Gym — CI/CD DevOps Pipeline

This project demonstrates a fully automated CI/CD pipeline for a modular Flask web application built for ACEest Fitness & Gym. It integrates testing, containerization, code quality analysis, and deployment using modern DevOps tools.

---

## 🚀 Tech Stack

- **Flask** — Modular Python web framework
- **Pytest** — Automated unit testing
- **Docker** — Containerization of the app and test environment
- **Jenkins** — CI/CD orchestration
- **SonarQube** — Code quality and coverage analysis
- **Git & GitHub** — Version control and remote repository
- **Minikube (Kubernetes)** — Optional deployment target

---

## 🛠️ Pipeline Stages

1. **Build Docker Image**
   - Creates a container for the Flask app with all dependencies

2. **Run Tests**
   - Executes Pytest inside the container
   - Generates coverage report (`coverage.xml`)

3. **SonarQube Analysis**
   - Scans code for bugs, vulnerabilities, and code smells
   - Uses coverage data for quality metrics

4. **(Optional) Deployment**
   - Deploys to Kubernetes via Minikube or Docker Compose

---

## 📂 Project Structure

ACEest_Fitness/
├── app/                  # Flask app modules
│   └── init.py
├── tests/                # Pytest test cases
│   └── test_routes.py
├── Dockerfile            # Container build instructions
├── Jenkinsfile           # CI/CD pipeline definition
├── sonar-project.properties
├── requirements.txt
└── README.md

---

## ✅ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/harshad141/ACEest_Fitness.git
cd ACEest_Fitness
```

### 2. Build and Test Locally
```bash
docker build -t aceest-flask-app .
docker run --rm aceest-flask-app /bin/bash -c "
    source venv/bin/activate &&
    pytest --cov=app --cov-report=xml
"
```
### 3. Run Jenkins Pipeline
Ensure Jenkins is running and configured with:
- SonarQube server and scanner
- Java 17 installed and registered
- GitHub webhook (optional)

Then push changes to trigger the pipeline:
```bash
git push origin main
```

## 📊 SonarQube Dashboard

After your Jenkins pipeline runs the SonarQube analysis stage, you can view detailed code quality metrics on your local SonarQube server.

### 🔗 Access Dashboard

### 📈 Metrics Tracked
- **Code Coverage** — via `coverage.xml` from Pytest
- **Bugs & Vulnerabilities** — static analysis of Python code
- **Code Smells** — maintainability issues
- **Duplications** — repeated logic or structure
- **Complexity** — cyclomatic and cognitive complexity scores

### 🧪 Quality Gate
You can configure a quality gate in SonarQube to enforce minimum standards (e.g., 80% coverage, 0 critical bugs). Jenkins can be set to fail the build if the gate is not passed.

> Tip: Use the `sonar-project.properties` file to customize project metadata and coverage paths.
