import os
import subprocess
import time

# Define some colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RED = '\033[91m'
END = '\033[0m'

# Print a header
print(f"{GREEN}Termux Advanced Installer{END}")
print(f"{YELLOW}================================={END}")

# Function to print a message with a spinning wheel
def print_spinning_message(message):
    for i in range(5):
        print(f"{BLUE}{message} {'|' if i == 0 else '/' if i == 1 else '-' if i == 2 else '\\' if i == 3 else '|'}{END}", end='\r')
        time.sleep(0.2)

# Install Git
print_spinning_message("Installing Git...")
os.system("pkg install -y git")
print(f"{GREEN}Git installed!{END}")

# Install Curl
print_spinning_message("Installing Curl...")
os.system("pkg install -y curl")
print(f"{GREEN}Curl installed!{END}")

# Install essential packages
print_spinning_message("Installing essential packages...")
os.system("pkg update && pkg upgrade -y")
os.system("pkg install -y python python-dev python-pip")
print(f"{GREEN}Essential packages installed!{END}")

# Install development tools
print_spinning_message("Installing development tools...")
os.system("pkg install -y build-essential cmake gcc g++ clang")
os.system("pkg install -y python3 python3-dev python3-pip")
print(f"{GREEN}Development tools installed!{END}")

# Install programming languages
print_spinning_message("Installing programming languages...")
os.system("pkg install -y nodejs npm")
os.system("pkg install -y ruby ruby-dev")
os.system("pkg install -y perl perl-dev")
os.system("pkg install -y java openjdk-8-jdk")
print(f"{GREEN}Programming languages installed!{END}")

# Install modern shell and terminal
print_spinning_message("Installing modern shell and terminal...")
os.system("pkg install -y fish")
os.system("pkg install -y kitty")
print(f"{GREEN}Modern shell and terminal installed!{END}")

# Configure Termux to use a colorful interface
print_spinning_message("Configuring Termux...")
os.system("echo 'PS1=\"\[\e[1;32m\]\u@\h\[\e[0m\]:\[\e[1;34m\]\w\[\e[0m\]\$ \"' >> ~/.bashrc")
os.system("source ~/.bashrc")
print(f"{GREEN}Termux configured!{END}")

# Create a GitHub repository for Termux-Advanced
print_spinning_message("Creating GitHub repository...")
subprocess.run(["git", "init"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial commit"])
subprocess.run(["git", "remote", "add", "origin", "https://github.com/ChefAdorous/Termux-Advanced.git"])
subprocess.run(["git", "push", "-u", "origin", "master"])
print(f"{GREEN}GitHub repository created!{END}")
