from datetime import date
import json
task_list = []  # convert this to dict


class OptionError(Exception):
    """Invalid Option"""


def save_task():
    with open('tasks.json','r') as file:
        json.dump(task_list,file,indent = 4,sort_keys=False)


def load_task():
    try:
        with open('tasks.json','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return [] 



def list_all_task(task_list):
    # print(task_list)
    with open("tasks.txt", "r") as file:
        for idx, line in enumerate(file, start=1):
            print(f"{idx}:{line}")


def add_task(tasks_list):
    task_desc = input("Enter a task: ")
    task_id = len(task_list)+1
    task = {
        "task_id":task_id,
        "task_description":task_desc,
        "date_added":str(date.today()),
        "date_updated":str(date.today()),
        "status":False
    }
    task_list.append(task)
    save_task(task_list)


def delete_task():
    list_all_task()
    option = input("enter task no. to delete: ")
    if (int(option) - 1) >= len(task_list):
        # raise ValueError(f"invalid {option=}")
        raise OptionError(f"invalid {option=}")
    else:
        popped_item = task_list.pop(int(option) - 1)
        print(f'"{popped_item}" has been deleted')
        save_task()


def mark_task():
    list_all_task()
    option = input("enter task no. to mark complete: ")
    if ((int(option) - 1) < 0) | ((int(option) - 1) >= len(task_list)):
        raise OptionError(f"Invalid {option=}")
    else:
        for idx, task in enumerate(task_list):
            if idx == int(option) - 1:
                # print(f'{task} "\u2705"')
                task_list[idx] = f"{task} \u2705 updated on {date.today()} "

    print(task_list)
    save_task()
    # print("\u2705")


# over this func we can use time module to mark the date and time of when the task was completed.
def main():
    load_task()
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


if __name__ == "__main__":
    main()
