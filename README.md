# Task-Management-System
This Python script is a Task Management System that allows users to manage tasks efficiently.

# English

- This code defines a class-based task management application using SQLite for storing data. It includes features like:

 - Add Task: Allows users to add a new task with a unique ID, description, registration date, and an optional desired date.

- Remove Task: Lets users delete a task by its unique ID.

- Update Task: Provides functionality to modify an existing task's details.

- View Tasks: Displays all stored tasks, including their description, registration date, and desired date.

- Save and Quit: Safely closes the database and exits the program.

# Key Features:

1. Database Management: The SQLite database (tasks.db) ensures data persistence.

2. Date Handling: Utilizes datetime.date to record task dates.

3. Error Handling: Includes prompts for valid inputs to avoid errors.

4. Random IDs: Generates random IDs for unique task identification.
