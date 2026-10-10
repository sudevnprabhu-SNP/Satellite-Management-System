# 🛰️ Satellite Management System

**A space-themed Python console application for managing satellite records, monitoring fuel levels, and tracking operational status.**

A beginner-friendly project that applies Python data structures and programming concepts to a space-science-inspired management system.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Dependencies-None-2ea44f?style=for-the-badge" alt="No third-party dependencies">
  <img src="https://img.shields.io/badge/Interface-CLI-555555?style=for-the-badge" alt="Command-line interface">
  <img src="https://img.shields.io/badge/Project-Learning%20Project-orange?style=for-the-badge" alt="Learning project">
</p>

---

## 🌌 Overview

The **Satellite Management System** is a menu-driven Python application designed to organize and manage satellite records through an interactive terminal interface.

Users can register satellites, search and filter records, update information, manage fuel levels, and view summary statistics. The project demonstrates how fundamental Python concepts can be applied to a domain inspired by satellite operations.

## ✨ Features

| Feature | Description |
|---|---|
| 🛰️ Satellite Registration | Add new satellite records with automatically generated IDs |
| 📋 Record Management | View, sort, and filter satellite records |
| 🔎 Search | Find satellites using their IDs and supported record fields |
| ✏️ Information Updates | Modify satellite details and operational status |
| ⛽ Fuel Management | Refuel satellites and simulate fuel consumption with range checks |
| 🗑️ Record Deletion | Remove satellite records with confirmation details |
| 📊 Statistics | Display summary information about the satellite collection |
| ⚠️ Status Warnings | Identify satellites with low fuel levels or older records |

## 🛠️ Built With

- **Language:** Python
- **Interface:** Command-line menu
- **Data storage:** Python dictionaries and in-memory records
- **Dependencies:** Python standard library only

No external packages or database setup are required.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or newer recommended
- A terminal or command prompt
- Git, if cloning the repository

### 1. Clone the repository

```bash
git clone https://github.com/sudevnprabhu-SNP/Satellite-Management-System.git
```

### 2. Open the project directory

```bash
cd Satellite-Management-System
```

### 3. Run the application

```bash
python3 src/Satellite_Management.py
```

Follow the on-screen menu to explore the available operations.

> **Windows users:** If `python3` is not recognized, try `python` instead.

## 🧪 Example Workflow

A typical session might involve:

1. Viewing the preloaded satellite records.
2. Searching for a satellite by its ID.
3. Updating its information or operational status.
4. Simulating fuel consumption or refuelling.
5. Reviewing summary statistics and warnings.

A sample Cartosat-3 record is included in the application.

## 📁 Project Structure

```text
Satellite-Management-System/
├── src/
│   └── Satellite_Management.py
├── docs/
│   └── screenshots/
│       └── README.md
├── README.md
├── requirements.txt
└── LICENSE
```

## 🖥️ Screenshots

Screenshots will be added after capturing actual application output.

Recommended screenshots:

- Main menu
- Satellite record listing
- Search results
- Fuel management
- Summary statistics

## 📌 Current Limitations

- **Temporary storage:** Records are held in memory and are lost when the program exits.
- **Simplified validation:** Checks are intended for learning and are not authoritative satellite-data validation.
- **Terminal interface:** The application does not currently provide a graphical user interface.
- **No external integration:** It does not connect to a database, satellite tracking service, or mission-control system.

This is an educational software project, not an operational satellite-control or mission-planning tool.

## 🎯 Learning Objectives

This project provides practical experience with:

- Python dictionaries and data structures
- Functions, loops, and conditional logic
- Input validation and menu-driven programming
- Searching, sorting, and filtering records
- Basic resource tracking and summary statistics
- Organizing a Python project for GitHub

## 🔮 Future Improvements

Potential extensions include:

- Persistent storage using SQLite
- A graphical interface or web dashboard
- More robust validation and automated tests
- Integration with publicly available satellite catalogue data
- Visual summaries of satellite records and fuel levels

These are **future possibilities**, not features currently implemented.

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

The license should be used only if you have the rights to license the code and documentation in this repository. Third-party materials, if added later, remain subject to their own terms.

---

<p align="center">
  <i>Built with Python • Inspired by Space Science • Created as a Learning Project</i>
</p>
