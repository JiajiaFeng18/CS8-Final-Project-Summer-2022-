# Task Management System

## Overview
This project is a Python-based Task Management System that allows users to create, update, filter, and delete tasks. The system provides persistent storage of tasks using CSV files, enabling users to save and restore their tasks across sessions. The project emphasizes user input validation to ensure the accuracy and consistency of task data.

## Features
- **Add Tasks**: Create new tasks with details such as name, priority, due date, and completion status.
- **Update Tasks**: Modify task attributes including name, priority, and completion status.
- **List Tasks**: View all tasks or filter tasks by their status (e.g., completed, incomplete).
- **Delete Tasks**: Remove individual tasks or clear all tasks from the system.
- **Persistent Storage**: Tasks are saved to a CSV file, allowing users to restore tasks in future sessions.
- **Input Validation**: Ensures correct formats for task names, priorities, due dates, and completion statuses.

## How to Use
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-repo/task_management_system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd task_management_system
   ```
3. Run the system:
   ```bash
   python task_system.py
   ```
4. Follow the on-screen menu to add, update, delete, or list tasks.

## Prerequisites
- **Python 3.x**: Make sure Python is installed on your system.
- **CSV Module**: The project uses Python's built-in `csv` module for file handling.

## File Structure
- `task_system.py`: The main file that runs the task management system.
- `task_functions.py`: Contains helper functions to manage task operations.
- `task_tests.py`: Unit tests to ensure the accuracy of the system's functions.
- `tasks.csv`: Stores tasks persistently.

## Future Enhancements
- **Task Categories**: Adding functionality to group tasks into different categories (e.g., work, personal).
- **Notification System**: Implementing reminders or notifications for tasks with upcoming due dates.
- **Task Prioritization**: Enhance the system to automatically suggest priority levels based on task urgency.
