# 🛡️ Cassinovey AI - Intelligent Recon & Vulnerability Scanner

Developed by **Rohith PR (Rosario)** *Independent Security Researcher | Cybersecurity Student (CICSA)*

---

## 🚀 Overview
**Cassinovey AI** is a specialized reconnaissance and attack surface mapping tool. It combines traditional security scanning methodologies with local AI (Ollama) to provide intelligent insights into potential vulnerabilities like SSRF, IDOR, and Business Logic flaws.

## ✨ Key Features
* **AI-Driven Analysis:** Automatically analyzes targets using local LLMs (TinyLlama/Custom Models).
* **Infrastructure Recon:** Rapidly identifies subdomains and web assets.
* **Advanced Bug Hunting:** Tailored for identifying complex security vulnerabilities.
* **Automated Setup:** Comes with a dedicated shell script for one-click installation.

---

## 🛠️ Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/rohithkichu818-collab/cassinovey-ai-recon-tool.git](https://github.com/rohithkichu818-collab/cassinovey-ai-recon-tool.git)
    cd cassinovey-ai-recon-tool
    ```

2.  **Run the Setup Script:**
    This script will install all dependencies, Python libraries, and the Ollama AI engine.
    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```

---

## 🖥️ Usage

1.  Ensure **Ollama** is running in the background:
    ```bash
    ollama run tinyllama
    ```

2.  Run the scanner:
    ```bash
    python3 cassinovey.py
    ```

---

## 👨‍💻 About the Author
I am **Rohith PR**, a cybersecurity enthusiast pursuing the **CICSA** course at RedTeam Hacker Academy. My focus is on offensive security, penetration testing, and building AI-integrated security tools to streamline the bug-hunting process.

* **GitHub:** [rohithkichu818-collab](https://github.com/rohithkichu818-collab)
* **Interests:** Bug Bounty, Red Teaming, Python Automation.

---

## ⚖️ License
This project is licensed under the **GPL-3.0 License**. For educational and ethical security testing only.
