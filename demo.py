from datetime import date


# task_desc = input("enter a task: ")
# task_dict = {
#     1: {
#         "task_desc": task_desc,
#         "date_added": date.today(),
#         "date_updated": date.today(),
#         "status": 0,
#     },
#     2: {
#         "task_desc": "water",
#         "date_added": date.today(),
#         "date_updated": date.today()
#     },
# }

# task_list.append(task_dict)

# print(type(task_dict))
# print(type(task_list))
# print(task_dict.get(2))
# print(task_list)
# # print(task_dict[1]["task_desc"])


print({i:i for i in range(1,10)})
task_list = []  
task_dict = {}

def add_task(task_list):
    task_desc = input("enter a task: ")
    task_dict={
        i:{
        "task_desc":task_desc,
        "date_added":date.today(),
        "date_updated":date.today(),
        "status":bool(0)
    }for i in range(1,2)}

    # print(task_dict)

    task_list.append(task_dict)

    print(task_dict)    
    print(task_list)  
    save_task(task_list)
    
def save_task(task_list):
    with open('tasks.json','w') as file:
        file.write(str(task_list))

def load_tasks():
    try:
        with open('task.json','r') as file:
            for task in file:
                task_list.append(task)
    except FileNotFoundError :
        return []





add_task(task_list)
load_tasks()
add_task(task_list)   
print(task_list)  
# print(task_list[0][1])

# task_id = 1
# # update_task(1)

