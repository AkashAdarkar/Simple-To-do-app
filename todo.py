task_list = []


def list_all_task():
    # print(task_list)
    with open("tasks.txt","r") as file:
        for idx,line in enumerate(file,start = 1):
            print(f"{idx}:{line}")
# read this from file rather this non-persistent list


def add_task():
    task = input("enter your task:")
    task_list.append(task)

    print(task_list)

    
    # list_all_task()
    


def delete_task():
    option = input("enter an index: ")
    task_list.pop(int(option))
    


def mark_task():
    print("\u2705")

def save_task():
    with open ("tasks.txt","a") as file: # save the list to a file
        file.write("\n".join(task_list)) #list->str
        file.write("\n")
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
