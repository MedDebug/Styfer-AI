# Styfer AI 🤖

Styfer AI is my personal assistant project built entirely in Python.

The goal of Styfer is to gradually evolve from a simple file manager into a full-featured AI assistant capable of managing files, remembering user information, automating tasks, and eventually interacting with AI models.

This project is being built step-by-step as a learning journey, with each version introducing new programming concepts and features.

---

## Current Features

### 📁 File Manager

* List all folders in the current directory
* List all files in the current directory
* Create folders
* Delete files
* Change directories
* Rename files and folders
* Search for files and directories using `os.walk()`

### 🧠 Memory Manager

* Create a persistent memory file using JSON
* Load memory on startup
* View stored memory
* Add new memory entries
* Edit existing memory entries
* Delete memory entries
* Protected core fields (such as username and age)

### 🛠 Technical Concepts Used

* Functions
* Modules and imports
* JSON storage
* File handling
* Error handling (`try` / `except`)
* Dictionaries
* Loops
* `os` module
* `os.walk()`

---

## Project Structure

```text
Styfer AI/
│
├── main.py
├── main_menu.py
│
├── file_main.py
├── file_menu.py
├── file_manager.py
│
├── memory_main.py
├── memory_menu.py
├── memory_manager.py
│
├── memory.json
└── README.md
```

---

## Future Plans

* Text file reader
* Login system
* Voice commands
* AI integration
* Task automation
* System monitoring
* Natural language command processing
* GUI interface

---

## Why I Built This

I wanted a project that would force me to learn real programming concepts instead of only solving coding problems.

Styfer is my long-term project where I practice software design, project structure, Git, file handling, JSON, and eventually AI development.

Every feature is written and expanded manually as I learn new concepts.

---

## Status

🚧 Work in Progress

Current Version: v0.6
