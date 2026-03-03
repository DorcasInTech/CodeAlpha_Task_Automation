This project is an automated file management solution developed during my Python Programming Internship at CodeAlpha. The script is designed to declutter workspace directories by automatically identifying, filtering, and moving image files into a dedicated folder.

Key Features
Multi-Format Detection: Automatically scans for and identifies .jpg, .jpeg, and .png files.
Here's the README for Task Automation:

---

**CodeAlpha - Task Automation with Python Scripts**

**Project Overview**

This is a Python-based File Automation Script developed as part of my internship at CodeAlpha. The application automatically scans a source folder and moves all image files into a dedicated organized folder, eliminating the need for manual file sorting.

**Features**
- Multi-Format Detection: Automatically identifies and moves .jpg, .jpeg, and .png files.
- Automated Directory Management: Creates the destination folder automatically if it doesn't exist.
- Safe File Relocation: Uses Python's shutil library to move files without risking data corruption.
- Completion Feedback: Prints a confirmation message for each file successfully moved.

**How to Run**
1. Ensure you have Python 3.x installed.
2. Clone this repository or download the `Automation_Script.py` file.
3. Place your image files inside the `my_files` folder.
4. Open your terminal or VS Code.
5. Run the script using the command:
```
python Automation_Script.py
```

**Technologies Used**
Language: Python 3
Libraries: os, shutil
Version Control: Git & GitHub
IDE: Visual Studio Code (VS Code)

Developed by Samson Dorcas as part of the CodeAlpha Software Development Internship.
Automated Directory Management: Programmatically checks for the existence of a destination folder and creates it if it's missing.

Safe File Relocation: Uses high-level shell utilities to move files without risking data corruption.

Technical Implementation
This script leverages Python's built-in standard libraries to interact with the system's file architecture:

os Library: Used for directory navigation and handling file paths to ensure the script works on Windows, macOS, and Linux.

shutil Library: Utilized for its robust file-moving operations.

How It Works
The script targets a source folder (e.g., my_files).

It loops through every file and checks for valid image extensions.

It joins the file path and moves the validated images to the organized_images folder.

Organization: CodeAlpha

Role: Python Programming Intern

Task: 03 - Task Automation
