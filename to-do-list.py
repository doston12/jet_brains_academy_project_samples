# To Do list project - stage 1/4

class Task:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def print_tasks(self):
        pass

class SubTask(Task):
    pass


t = Task()
st = SubTask()
print(type(st) == SubTask)
print(isinstance(st, Task))


def print_tasks():
    print("""Today:
1) Do yoga
2) Make breakfast
3) Learn basics of SQL
4) Learn what is ORM""")

print_tasks()