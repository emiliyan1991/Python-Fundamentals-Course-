command = input()
todo = ["" for i in range(11)]
while command != "End":
    cmd = command.split("-")
    priority = int(cmd[0])
    task = cmd[1]
    todo[priority] = task
    command = input()

final_todo = [job for job in todo if job != ""]
print(final_todo)
