This project is an automated file management solution developed during my Python Programming Internship at CodeAlpha. The script is designed to declutter workspace directories by automatically identifying, filtering, and moving image files into a dedicated folder.

Key Features
Multi-Format Detection: Automatically scans for and identifies .jpg, .jpeg, and .png files.

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