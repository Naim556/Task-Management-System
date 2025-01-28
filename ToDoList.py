import random
from datetime import date
import sqlite3

class ToDoList:
    def __init__(self):
        super().__init__()
        self.months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        self.conn = sqlite3.connect("Data\\tasks.db")
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        # Data Base
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                registration_date TEXT NOT NULL,
                desired_date TEXT
            )
        """)
        self.conn.commit()

    def additem(self,):
        print("Add a new task. Follow the prompts:")

        # Using a random number for the ID
        task_id = random.randrange(100000, 999999)
        task_description = input("Please enter your desired task: ")

        # Task registration date
        registration_date = date.today().strftime("%Y-%B-%d")
        desired_date = self.get_desired_date()

        task = (f"ID : {task_id}\n"
               f"Task : {task_description}\n"
               f"Registration date : {registration_date}\n")

        self.cursor.execute("""
                    INSERT INTO tasks (id, description, registration_date, desired_date)
                    VALUES (?, ?, ?, ?)
                """, (task_id, task_description, registration_date, desired_date))
        self.conn.commit()

    def get_desired_date(self, optional=False):
        if optional:
            # Accepts any answer except yes as no.
            choice = input("Do you want to update the desired date? (yes/no): ").strip().lower()
            if choice not in ["yes", "y"]:
                return None

        while True:
            # Check the entered number.
            year = self.get_valid_int("Enter the desired year (or 0 to skip): ")
            if year == 0 and optional:
                return None

            # Checks the entered month, which must match one of the 12 months.
            month = input("Enter the desired month: ").strip().capitalize()
            if month not in self.months:
                print("Invalid month. Try again.")
                continue
            # check the day valid int and between 1 and 31
            day = self.get_valid_int("Enter the desired day (1-31): ")
            if 1 <= day <= 31:
                return f"{year}-{month}-{day}"

            print("Invalid day. Try again.")

    def removeitem(self,):
        # If you entered the information incorrectly, you can delete it.
        print("In this section, you can delete items you entered incorrectly.")
        task_id = self.get_valid_int("Enter the task ID to remove: ")
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Task {task_id} removed.")
        else:
            print("Task ID not found.")

    def update_item(self):
        # If you have entered the information incorrectly, you can change it by accessing the entered information.
        task_id = self.get_valid_int("Enter the task ID to update: ")
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        task = self.cursor.fetchone()

        if task:
            print("Current task details:")
            self.display_task(task)

            new_description = input("Enter the new description (or press Enter to keep current): ")
            if not new_description:
                new_description = task[1]

            new_date = self.get_desired_date(optional=True)
            if not new_date:
                new_date = task[3]

            self.cursor.execute("""
                UPDATE tasks
                SET description = ?, desired_date = ?
                WHERE id = ?
            """, (new_description, new_date, task_id))
            self.conn.commit()
            print("Task updated.")
        else:
            print("Task ID not found.")

    def display_tasks(self):
        # show the all task.
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()

        if not tasks:
            print("No tasks available.")
        for task in tasks:
            self.display_task(task)

    def display_task(self, task):
        # show the one task
        print(f"ID: {task[0]}")
        print(f"  Description: {task[1]}")
        print(f"  Registration Date: {task[2]}")
        desired_date = task[3] or "None"
        print(f"  Desired Date: {desired_date}")

    def saveandquit(self):
        self.conn.close()
        print("Tasks saved. Goodbye!")
        quit()

    def get_valid_int(self, prompt):
        # In this section, we will check your input to make sure the number is entered.
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

    def userselect(self, user_choice):
        # In this section, you must enter a number from 1 to 5 to access other factors.
        if user_choice == 1:
            self.additem()
        elif user_choice == 2:
            self.removeitem()
        elif user_choice == 3:
            self.update_item()
        elif user_choice == 4:
            self.display_tasks()
        elif user_choice == 5:
            self.saveandquit()
        else:
            print("Please enter a number between 1 and 5.")

def start_program():
    start = ToDoList()
    print("Menu: \n"
          "\t1. Add Item\n"
          "\t2. Remove Item\n"
          "\t3. change Item\n"
          "\t4. Show Item\n"
          "\t5. Save and Quit\n")

    while True:
        choice = start.get_valid_int("Select an option (1-5): ")
        start.userselect(choice)


if __name__ == "__main__":
    text = ("Hi, I am Naeem. This project is a personal project for task management.\n"
            "In this code, you can use date and time to complete your tasks at the specified time.\n")
    print(text)
    start_program()

