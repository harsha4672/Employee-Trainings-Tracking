# Employee Trainings Tracker Console Application

This repository contains a console application developed as part of the programming exercise for the Application Developer position at the University of Illinois Urbana-Champaign. The application reads training data from a `.json` file and generates outputs based on user requests. It supports interactive features to count completed trainings, list participants based on fiscal year, and check for expired or soon-to-expire trainings.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage Instructions](#usage-instructions)
- [Application Output](#application-output)
- [Repository Structure](#repository-structure)
- [Running the Application](#running-the-application)
- [Requirements](#requirements)

## Overview

The application processes training data stored in a `.json` format (or uses the default file `trainings.txt`) to achieve the following:
1. Count the number of people who completed each distinct training.
2. List all people who completed a specific set of trainings in a given fiscal year.
3. Find people with expired or soon-to-expire trainings based on a specified date.

## Features

- **Task 1:** Displays the count of people who completed each training.
- **Task 2:** Lists people who completed specified trainings within a given fiscal year.
- **Task 3:** Lists people whose trainings have expired or will expire within one month of a given date.

## Usage Instructions

1. **Provide a custom `.json` file or use the default training data** (`trainings.txt`).
2. **Task Selection:** The user can select a task from a menu:
   - Count completed trainings.
   - List people by fiscal year.
   - Find expired or soon-to-expire trainings.
   - Exit the application.

## Application Output

### Example Input

You can either input your own `.json` file with training records or use the default file (`trainings.txt`). The application prompts you for your preferred task and any relevant information needed (like fiscal year or date).

### Example Output

The output is shown as JSON-formatted data for each task. Example results for each task are stored in the repository as:

- `completed_counts.json`: Contains the number of people who completed each training.
- `trainings_in_fiscal.json`: Contains a list of people who completed specific trainings in a fiscal year.
- `expired_trainings.json`: Contains a list of people whose training has expired or is about to expire within one month.

## Repository Structure

```
├── README.md           # This readme file
├── trainings.txt       # Default input file for training records in JSON format
├── completed_counts.json   # Output file for Task 1
├── trainings_in_fiscal_year.json   # Output file for Task 2
├── expired_trainings.json   # Output file for Task 3
└── tracking_app.py              # Main Python script for the console application
```

## Running the Application

1. Clone this repository:
    ```bash
    git clone https://github.com/harsha4672/Employee-Trainings-Tracking.git
    cd Employee-Trainings-Tracking
    ```

2. Run the application:
    ```bash
    python tracking_app.py
    ```

3. Follow the interactive prompts in the console to perform tasks.

## Requirements

- Python 3.x
- JSON library (built-in with Python)
- `trainings.txt` file (default data) or a custom training data JSON file
