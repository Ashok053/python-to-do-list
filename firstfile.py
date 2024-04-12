Tasks = []


def addtask():
    task = input("enter task to add in list")
    Tasks.append(task)
    print(f"task \"{task}\" added to list")


def showlist():
    if not Tasks:
        print("no item is added to list")
    else:
        print("current task: ")
        for index, task in enumerate(Tasks):
            print(f"task #{index}. {task}")


def deletetask():
    showlist()
    from logging import exception
    try:
        tasktodelete = int(input("enter the # to delete"))
        if tasktodelete < len(Tasks):
            Tasks.pop(tasktodelete)
            print(f"task #{tasktodelete} is removed successfully")
        else:
            print(f"task #{tasktodelete} is not found")
    except exception:
        print("invalid input.")


print('***Welcome to our todo list***')
while True:
    print("\n")
    print("select your operation\n")
    print("1. add task")
    print("2. delete task")
    print("3. show list")
    print("4. quit")

    choice = int(input("enter your choice"))
    if choice == 1:
        addtask()
    elif choice == 2:
        deletetask()
    elif choice == 3:
        showlist()
    elif choice == 4:
        break
    else:
        print("invalid input, try again")
