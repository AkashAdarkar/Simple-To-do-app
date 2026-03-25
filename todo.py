def list_all_task():
    pass

def add_task():
    pass

def mark_task():
    pass




while True:
    print("A To-Do App")
    print("""1\t list all tasks \n2\t add new tasks \n3\t mark as completed \n4\t exit""")
    
    option = input("select an option: ")
    match option:
        case '1':
            list_all_task()
        case '2':
            add_task()
        case '3':
            mark_task
        case '4':
            break
    