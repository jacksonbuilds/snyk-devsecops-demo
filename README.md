# 🛡️ DevSecOps Demo: Snyk Integration with Python, Docker & GitHub Actions

This project demonstrates how to integrate [Snyk](https://snyk.io/) into a modern DevSecOps pipeline for detecting vulnerabilities in both **application dependencies** and **Docker containers**. It showcases real-world security automation practices using:

- ✅ Snyk CLI for local and CI-based vulnerability scanning
- 🐳 Docker for containerization
- 🐍 Flask-based Python application (intentionally vulnerable)
- ⚙️ GitHub Actions for continuous security testing
- ⚡ Ansible (optional) for infrastructure automation

---

## 🚀 Project Objectives

- Integrate **Snyk CLI** with a Python/Docker project
- Automate security scans in a **CI/CD pipeline**
- Demonstrate **shift-left security** using real tooling
- Showcase a **DevSecOps skillset** using open-source components

---

## 📁 Project Structure

```text
snyk-devsecops-demo/
│
├── app/                    # Vulnerable Flask app
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── ansible/                # (Optional) Ansible playbook for deployment
│   └── deploy.yml
│
├── scripts/                # Custom scripts for reporting/demo (Mock API Integration)
│   └── report_upload.py
│
├── .github/workflows/      # CI pipeline
│   └── snyk-analysis.yml
│
├── snyk/                   # Optional policy or test exclusions
│   └── snyk.policy
│
└── README.md
```

🧪 Vulnerability Scanning with Snyk CLI
▶️ Run Locally
```
Scan Python Dependencies
snyk test --file=app/requirements.txt --command=python3

Scan Docker Image
docker build -t snyk-test-app ./app
snyk test --docker snyk-test-app
```

⚙️ GitHub Actions Integration

On every commit or pull request, the GitHub Actions workflow:

    Installs the Snyk CLI

    Authenticates via the SNYK_TOKEN secret

    Builds the Docker image

    Scans both dependencies and the Docker image

🔐 Setting Up Snyk

    Create a free Snyk account

    Get your Snyk API token under Account Settings

    Add it to your GitHub repo:

        Go to Settings → Secrets and Variables → Actions

        Add a secret: SNYK_TOKEN

🛠️ Technologies Used
```
Category	Tools & Frameworks
Programming	Python, Flask
Security Scanning	Snyk CLI
Containerization	Docker
CI/CD Automation	GitHub Actions
Config Management	Ansible (optional use case)
Scripting & APIs	Python, Bash
```

✅ What This Demonstrates
```
✔️ DevSecOps pipeline design
✔️ Snyk integration with local and CI workflows
✔️ Container image scanning
✔️ GitHub Actions security automation
✔️ Secure coding & vulnerability awareness
```

📷 Sample Output
```
✗ Medium severity vulnerability found in requests@2.19.1
  Description: Arbitrary Code Execution
  Info: https://snyk.io/vuln/SNYK-PYTHON-REQUESTS-72435

```

# License
This project is licensed under the MIT License. See LICENSE for details.