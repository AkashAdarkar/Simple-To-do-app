task_list = []

with open("tasks.txt","r") as file:
    for line in file:
        task_list.append(line.replace("\n",""))

print(task_list)

def list_all_task():
    # print(task_list)
    with open("tasks.txt","r") as file:
        for idx,line in enumerate(file,start = 1):
            print(f"{idx}:{line}")
# read this from file rather this non-persistent list


def add_task():
    with open("tasks.txt","a") as file :
        task = input("enter a task: ")
        file.write(task+'\n')
        task_list.append(task)
    # list_all_task()
    
def save_task():
    pass
#new bramch
def delete_task():
    list_all_task()
    option = input("enter task no. to delete: ")
    task_list.pop(int(option)-1)
    print(task_list)
    with open("tasks.txt","w") as file:
        for task in task_list:
            file.write(task+"\n")
            
    


def mark_task():
    list_all_task()
    option = input("enter task no. to mark complete: ")
    for idx ,task in enumerate(task_list):
        if idx == int(option)-1 :
            # print(f'{task} "\u2705"')
            task_list[idx] = f'{task} \u2705'

    print(task_list)
    with open('tasks.txt','w') as file:
        for task in task_list:
            file.write(task+'\n')
    # print("\u2705")




        
# over this func we can use time module to mark the date and time of when the task was completed.

while True:
    print("A To-Do App")
    print(
        """1\t list all tasks \n2\t add new tasks \n3\t mark as completed \n4\t delete task \n5\t exit"""
    )

    option = input("select an option: ")
    match option:
        case "1":
            list_all_task()
        case "2":
            add_task()
        case "3":
            mark_task()
        case "4":
            delete_task()
        case "5":
            save_task()
            break
