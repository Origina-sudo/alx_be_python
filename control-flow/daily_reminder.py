# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task’s priority (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide a customized reminder based on the priority and time sensitivity
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
    case 'low':
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority level"

if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print(reminder)

