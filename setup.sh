#!/bin/bash

# Cassinovey AI - Installation Script
# Developed by Rohith PR (Rosario)

echo -e "\e[1;34m[*] Starting Cassinovey AI Tool Setup...\e[0m"

# 1. Update system packages
echo -e "\e[1;32m[*] Updating system packages...\e[0m"
sudo apt update

# 2. Install Python and Pip if not exists
echo -e "\e[1;32m[*] Checking for Python and Pip...\e[0m"
sudo apt install python3 python3-pip -y

# 3. Install Python requirements
if [ -f "requirements.txt" ]; then
    echo -e "\e[1;32m[*] Installing Python dependencies...\e[0m"
    pip3 install -r requirements.txt
else
    echo -e "\e[1;31m[!] requirements.txt not found! Creating a basic one...\e[0m"
    echo "requests" > requirements.txt
    echo "ollama" >> requirements.txt
    pip3 install -r requirements.txt
fi

# 4. Check if Ollama is installed
if ! command -v ollama &> /dev/null
then
    echo -e "\e[1;33m[*] Ollama not found. Installing Ollama...\e[0m"
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo -e "\e[1;32m[*] Ollama is already installed.\e[0m"
fi

echo -e "\e[1;34m\n[+] Setup Complete, Rohith!\e[0m"
echo -e "\e[1;33m[!] To run the tool: python3 cassinovey.py\e[0m"
