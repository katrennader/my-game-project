My_Tasks=[]  # task list
from datetime import datetime

def check_due_date():
    while True:
        due_date = input("Enter task due date (Year-Month-Day): ")
        try:
            valid_date = datetime.strptime(due_date, "%Y-%m-%d")
            return valid_date.strftime("%Y-%m-%d") 
        except ValueError:
            print("Invalid date format or value. Please enter the date in Year-Month-Day format.")

def view_task(My_Taske):   #  function to diplay tasks 
    if not My_Taske:
        print("No tasks found.")
    else:
        for i, task in enumerate(My_Taske, start=1):
            print(f"Task {i}:")
            for key, value in task.items():
                print(f"  {key}: {value}")
   
def Add_task(My_Tasks):
  Adding = True
  while Adding : 
    print ("Add new task ")
    Description = input("Enter task decription: ")
    priority = input("Enter task priority (Low, Medium, High) write l or m or h => ").lower()
    if priority != "l" and priority != "m" and priority != "h":
      priority = input("invalid task priority , choice (Low, Medium, High) write l or m or h => ").lower()
    due_date = check_due_date()
    
    My_Tasks.append({"Description":Description, "Priority":priority, "Due_date":due_date})
    print("Task added successfully")
    Add_more = input("Do you want to add another task? (y/n): ").lower()
    if Add_more != 'y':
      Adding = False

def Update_task(My_Tasks):
    updating = True
    while updating:
        view_task(My_Tasks)
        tasknumber = int(input("Choose task number you want to update => "))  # task number starts from 1 but list is zero
        task = tasknumber - 1
        
        if task >= 0 and task <= len(My_Tasks) - 1:  # Valid task number check
            New_Description = input("Enter new task description: ")
            New_priority = input("Enter new task priority (Low, Medium, High) write l or m or h => ").lower()
            
            # Ensure valid priority
            while New_priority != "l" and New_priority != "m" and New_priority != "h":
                New_priority = input("Invalid task priority, choose (Low, Medium, High) write l or m or h => ").lower()

            New_due_date = check_due_date()  # Assuming check_due_date() is implemented elsewhere
            My_Tasks[task] = {"Description": New_Description, "Priority": New_priority, "Due_date": New_due_date}
            print("Task updated successfully.")
            
            # Ask if the user wants to update another task
            update_more = input("Do you want to update another task? (y/n): ").lower()
            if update_more != "y":
                updating = False  # Exit loop if user doesn't want to update more tasks
        else:
            print("Invalid task number.")
def Delete_task(My_Tasks):
  if not My_Tasks:
    print("No tasks available to delete.")
    return 
  view_task(My_Tasks)
  tasknumber = int (input("choose task number you want to delete => ")) # task number starts from 1 but list is zero 
  task = tasknumber -1  
  if task >=0 and task <= len(My_Tasks)- 1:
        My_Tasks.pop(task)
        print("Task deleted successfully.")
  else :
    print("Invalid task number.")

print ("- < - < Welcome Back My Friend  > - > - ")
def diplay_menu():
  print ("* * * * * * *  MENU  * * * * * * *\n1.View all tasks\n2.Add a new task\n3.Update a task\n4.Delete a task\n5.Exit")

running = True
while running:
      diplay_menu()
      try :
        choice = int(input("Choice (1, 2, 3, 4, 5): "))
        while choice <1 or choice >5 :
          def diplay_menu():
            choice = int(input("Choice (1, 2, 3, 4, 5): "))
        if choice == 1:
            view_task(My_Tasks)
        elif choice == 2:
            Add_task(My_Tasks)
        elif choice == 3:
            Update_task(My_Tasks)
        elif choice == 4:
            Delete_task(My_Tasks)
        elif choice == 5:
            print("Goodbye my friend, see you soon!")
            running = False
      except ValueError:
        print("Invalid input. Please choice (1, 2, 3, 4, 5)")  
        