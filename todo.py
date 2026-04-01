task_list = []
class OptionError(Exception):
    """Invalid Option"""

def save_task():
    with open('tasks.txt','w') as file:
        for task in task_list:
            file.write(task+'\n')

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
    # with open("tasks.txt","a") as file :
    task = input("enter a task: ")
    # file.write(task+'\n')
    task_list.append(task)
    save_task()
    list_all_task()
    

def delete_task():
    list_all_task()
    option = input("enter task no. to delete: ")
    if ((int(option)-1) >= len(task_list)):
        # raise ValueError(f"invalid {option=}")
        raise OptionError(f"invalid {option=} err from class")
    else:
        popped_item=task_list.pop(int(option)-1)
        print(f'\"{popped_item}\" has been deleted')
        save_task()

def mark_task():
    list_all_task()
    option = input("enter task no. to mark complete: ")
    if ((int(option)-1) < 0 )|((int(option)-1) >= len(task_list)):  
        raise OptionError(f"Invalid {option=}")
    else:
        for idx ,task in enumerate(task_list):
            if idx == int(option)-1 :
                # print(f'{task} "\u2705"')
                task_list[idx] = f'{task} \u2705'

    print(task_list)
    save_task()
    # print("\u2705")




        
# over this func we can use time module to mark the date and time of when the task was completed.

while True:
    
    print(
        """
A To-Do App
-------------------
1: list all tasks 
2: add new tasks 
3: mark as completed 
4: delete task 
5: exit"""
    )

    option = input("select an option: ")
    match option:
        case "1":
            list_all_task()
        case "2":
            add_task()
        case "3":
            try:
                mark_task()
            except OptionError as err:
                print(err)
                list_all_task()
        case "4":
            try:
                delete_task()
            # except ValueError as err:
            except OptionError as err:
                print(err)
                list_all_task()
        # case "5":
        #     save_task()
            # break
        case _:
            print("Invalid Option")
            break