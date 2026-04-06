# Python CLI Tool
<img src="https://socialify.git.ci/SefBitz/s.py/image?description=1&font=Jost&language=1&name=1&owner=1&pattern=Circuit+Board&stargazers=1&theme=Dark">
https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/discord.svg
This is a custom Python-based Command Line Interface (CLI) designed to be launched directly from a Bash terminal (Linux, macOS, or Git Bash on Windows).

<a href="https://discord.com/users/1275686951499857924"><img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/discord.svg></a>

## 🚀 Quick Start

Follow these three steps to get the script running on your machine:

### 0. Download the Repository
To get a copy of this script and all its files on your computer, use the `git clone` command in your Git Bash terminal:

`git clone https://github.com`

After cloning, move into the project directory:

cd your-repo-name

### 1. Prerequisites
Ensure you have Python 3 installed. 
* Windows Users: You must use Git Bash to run these commands.
* Mac/Linux Users: Use your standard terminal.

### 2. Set Permissions
Before running the script for the first time, you must give it "execute" permission. Open your terminal in the folder containing s.py and run:

`chmod +x s.py`

### 3. Run the Script
You can now launch the CLI directly using the ./ prefix:

`./s.py`

---

## 🛠 Features & Usage

### Passing Arguments
If the script accepts inputs, you can pass them just like a native Linux command:

`./s.py --option value`

### Script Requirements
For this to work as a standalone command, the s.py file must include the following "shebang" line at the very top:

`#!/usr/bin/env python3`

---

## 💡 Troubleshooting (Windows/Git Bash)

If you are using Git Bash and the script hangs or doesn't show output, Windows may be blocking the interactive terminal. Use winpty to force it:

`winpty ./s.py`

To avoid typing winpty every time, you can add this alias to your .bashrc file:
`alias s='winpty python s.py'`
  
