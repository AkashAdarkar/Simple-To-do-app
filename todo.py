def list_all_task():
    for task in task_list:
        print(task)
    

def add_task():
    task = input("")
    task_list.append(task)
    list_all_task()


def mark_task():
    pass




while True:
    task_list = []
    print("A To-Do App")
    print("""1\t list all tasks \n2\t add new tasks \n3\t mark as completed \n4\t exit""")
    
    option = input("select an option: ")
    match option:
        case '1':
            list_all_task()
        case '2':
            add_task()
        case '3':
            mark_task()
        case '4':
            break
    