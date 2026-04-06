# Python CLI Tool

<img src="https://socialify.git.ci/SefBitz/spyPY/image?description=1&font=Jost&forks=1&issues=1&language=1&name=1&owner=1&pattern=Circuit+Board&pulls=1&stargazers=1&theme=Dark">

<a href="https://discord.com/users/1275686951499857924">Discord</a>
<a href="https://youtube.com/@sefbitz">Youtube</a>


This is a custom Python-based Command Line Interface (CLI) designed to be launched directly from a Bash terminal (Linux, macOS, or Git Bash on Windows).

## What it does
- This CLI tool runs in 2 stages in order to fufill the requirements for development
#### Stage 1: Greeting
- The CLI at this stage will prompt the user with "Enter a string", where you are presented with 3 choices
  1. say 'hi': this will trigger a `print()` that responds and will cause the program to move unto the 2nd stage.
  2. say 'hello': this will also trigger the same response and moves the program forward. Please note that this stage is case insensitive.
  3. say something else: this response will trigger an unhappy response from the CLI, softlocking you and forcing you to restart the program. **please do not trigger this.**
 
#### Stage 2: Logging
- The CLI will now create a folder if you have not, if you have installed the program using the steps below, it should work well.
- The CLI will now prompt the user for a log input, which it will append along with the current time into the `log.txt` file. 
- You can type `exit` to exit this stage. 

## 🚀 Quick Start

Follow these three steps to get the script running on your machine:

### 0. Download the Repository
To get a copy of this script and all its files on your computer, use the `git clone` command in your Git Bash terminal:

`git clone https://github.com/SefBitz/spyPY`

After cloning, move into the project directory:

`cd spyPY`

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
  
