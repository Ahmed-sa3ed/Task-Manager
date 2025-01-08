import datetime
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "Tasks.json"
file_path = os.path.join(current_dir,file_name)

class Task:
    def __init__(self,ID=None,Description="",Status="Todo",CreatedAt=None,UpdatedAt=None):
        self.ID = ID
        self.Description = Description
        self.Status = Status
        if CreatedAt and UpdatedAt:
            self.CreatedAT = CreatedAt
            self.UpdatedAt = UpdatedAt
        else:
            self.CreatedAT = datetime.datetime.now().isoformat()
            self.UpdatedAt = datetime.datetime.now().isoformat()
        # self.Task_Store()

    def Update_Description(self,description):
        self.Description = description
        self.UpdatedAt = datetime.datetime.now().isoformat()
        print("Task Updated Successfully")
        self.Print_Task()

    def mark_in_progress(self):
        self.Status = "In-progress"
        self.UpdatedAt = datetime.datetime.now().isoformat()

    def mark_done(self):
        self.Status = "Done"
        self.UpdatedAt = datetime.datetime.now().isoformat()

    def Task_Store(self):
        return {"ID" : self.ID,
                "Description" : self.Description,
                "Status" : self.Status,
                "CreatedAt" : self.CreatedAT,
                "UpdatedAt" : self.UpdatedAt}
    
    def Print_Task(self):
        print("="*156)
        print("||"+"ID".center(30)+"||"+f"{self.ID}".center(120)+"||")
        print("_"*156)
        print("||"+"Description".center(30)+"||"+f"{self.Description}".center(120)+"||")
        print("_"*156)
        print("||"+"Status".center(30)+"||"+f"{self.Status}".center(120)+"||")
        print("_"*156)
        print("||"+"CreatedAt".center(30)+"||"+f"{self.CreatedAT}".center(120)+"||")
        print("_"*156)
        print("||"+"UpdatedAt".center(30)+"||"+f"{self.UpdatedAt}".center(120)+"||")
        print("="*156)
    


def get_task_ID(id,Task_List):
    for task in Task_List:
        if str(task.ID) == id:
            return task
    return None
    
def get_task_status(status,Task_List):
    St_tasks=[]
    for task in Task_List:
        if str(task.Status).lower() == str(status).lower():
            St_tasks.append(task)
    return St_tasks

def print_tasks(T_list):
    if T_list:
        for t in T_list:
            t.Print_Task()
    else:
        print("No Task available")

def delete_task(ID, task_list):
        task = get_task_ID(ID,task_list)
        if task:
            task_list.remove(task)
            print(f"The Task {ID}: {task.Description} is deleted ")
        else:
            print("This Task is not exist")

def read_tasks():
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            tasks = json.load(file)
            Task_List = [Task(**task) for task in tasks]
            Next_ID = max((task.ID for task in Task_List), default=0)+1
        return Task_List,Next_ID
    else:
        return [], 1

def write_tasks(Task_List):
    with open(file_path,'w',encoding='utf8') as file:
        tasks_dict = [task.Task_Store() for task in Task_List]
        json.dump(tasks_dict, file, indent=4, sort_keys=True, ensure_ascii=False)

def print_menu():
    print("Usage:")
    print("   add \"Task description\"")
    print("   update <id> \"New description\"")
    print("   delete <id>")
    print("   mark-in-progress <id>")
    print("   mark-done <id>")
    print("   list [done|todo|in-progress]")
    print("   Exit: To exit the program")

def input_error():
    print("!!! Input Error!!!")
    print("Please input your command as explained in the user guide")
    print_menu()

def print_welcome(Task_List):
    print("Welcome to My Task manager app")
    no_tasks = len(Task_List)
    print(f"You have {no_tasks} Tasks")
    if no_tasks:
        print_tasks(Task_List)



Next_ID = 1
Task_List = []
Task_List,Next_ID = read_tasks()
print_welcome(Task_List)
print_menu()
while 1:
    
    command = input("Enter Your Command:")
    fun = command.strip().split(" ")[0].lower()
    if fun == "exit":
        break
    elif fun == "add":
        des = command.strip().split('"')[1]
        Task_List.append(Task(ID=Next_ID ,Description=des)) if des else input_error()
        Next_ID += 1
        
    elif fun == "update":
        try:
            id = command.strip().split("<")[1].split(">")[0]
            des = command.strip().split('"')[1]
            t = get_task_ID(id,Task_List) if id.isalnum() else None
            if t:
                t.Update_Description(des) if des else input_error()
            else:
                print("Task not found")
        except (IndexError, ValueError):
            input_error()

    elif fun == "delete":
        try:
            id = command.strip().split("<")[1].split(">")[0]
            t = get_task_ID(id,Task_List) if id.isalnum() else None
            if t:
                delete_task(id,Task_List)
            else:
                print("Task not found")
        except (IndexError, ValueError):
            input_error()

    elif fun == "mark-in-progress":
        try:
            id = command.strip().split("<")[1].split(">")[0]
            t = get_task_ID(id,Task_List) if id.isalnum() else None
            if t:
                t.mark_in_progress()
            else:
                print("Task not found")
        except (IndexError, ValueError):
            input_error()
    
    elif fun == "mark-done":
        try:
            id = command.strip().split("<")[1].split(">")[0]
            t = get_task_ID(id,Task_List) if id.isalnum() else None
            if t:
                t.mark_done()
            else:
                print("Task not found")
        except (IndexError, ValueError):
            input_error()

    elif fun == "list":
        try:
            stat = command.strip().split("[")[1].split("]")[0].lower()
            if stat == "all":
                print_tasks(Task_List)
            elif stat in ["todo","in-progress","done"]:
                T_L = get_task_status(stat,Task_List)
                if T_L:
                    print_tasks(T_L)
                else:
                    print(f"No tasks with status '{stat}' found.")
            else:
                input_error()
        except (IndexError, ValueError):
            input_error()
    else:
        input_error()

write_tasks(Task_List)