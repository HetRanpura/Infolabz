# todo list
todo=["presentation","session","pay salary","develop code"]
print("Your todo list is:",todo)

#enter new task
new_task=input("enter new task: ")
todo.append(new_task)
print("updated todo list:",todo)

#remove completed task
completed_task=input("enter completed task: ")
todo.remove(completed_task)
print("updated todo list:",todo)
