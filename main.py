from tasks import PersonalTask, WorkTask, UrgentWorkTask, TaskManager

manager = TaskManager("Nudge")

# Create tasks with priority validation
try:
    TaskManager.validate_priority("Low")
    t1 = PersonalTask("Buy groceries", "Low", "Shopping")
except ValueError as e:
    print(f"Error: {e}")

try:
    TaskManager.validate_priority("Medium")
    t2 = PersonalTask("Clean house", "Medium", "Home")
except ValueError as e:
    print(f"Error: {e}")

try:
    TaskManager.validate_priority("High")
    t3 = WorkTask("Fix server", "High", "2024-12-01")
except ValueError as e:
    print(f"Error: {e}")

try:
    TaskManager.validate_priority("High")
    t4 = WorkTask("Write report", "High", "2024-12-05")
except ValueError as e:
    print(f"Error: {e}")

try:
    TaskManager.validate_priority("High")
    t5 = UrgentWorkTask("Emergency fix", "High", "2024-11-30", "System crash")
except ValueError as e:
    print(f"Error: {e}")

# Add tasks using method chaining
manager.add_task(t1).add_task(t2).add_task(t3).add_task(t4).add_task(t5)

# Call summary
manager.summary()

# Change status of one PersonalTask
t1.status = "done"

# Execute all tasks
for task in manager.tasks:
    task.execute()

# Filter and print only PersonalTasks
personal_tasks = manager.get_tasks_by_type(PersonalTask)
print("Personal Tasks:")
for task in personal_tasks:
    print(task)

# Print total tasks
print(f"Total tasks: {TaskManager.get_total_tasks()}")

# Try invalid status
try:
    t1.status = "invalid"
except ValueError as e:
    print(f"Status error: {e}")

# Try invalid priority validation
try:
    TaskManager.validate_priority("Invalid")
except ValueError as e:
    print(f"Priority error: {e}")