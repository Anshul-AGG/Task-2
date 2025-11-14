class ToDoList:

    def __init__(self, task=None):
        self.task = []
        if task:
            self.task.append(task)

    def add(self, new_task):
        if isinstance(new_task, str) and new_task.strip():
            self.task.append(new_task.strip())
            print("task added, ", new_task.strip())
        else:
            print("Invalid Input")

    def remove(self, task_name):
        try:
            self.task.remove(task_name.strip())
            print("task is removed, ", task_name.strip())
        except ValueError:
            print(f"error: {task_name.strip()} not found in the list")

    def view(self):
        print("Current tasks are: ")
        for index, task in enumerate(self.task):
            print(f"{index + 1}. {task}")

    def save_file(self, filename="tasks.txt"):
        try:
            with open(filename, "w") as f:
                for task in self.task:
                    f.write(task + "\n")

        except IOError as e:
            print(f"error saving tasks : {e}")


my_study_list = ToDoList("Start Apna College AI/ML course")
my_study_list.view()
my_study_list.add("Read chapter 1 on Python classes")
my_study_list.add("Set up virtual environment")
my_study_list.add("Review previous notes on SailPoint and Azure")
my_study_list.remove("Review previous notes on SailPoint and Azure")
my_study_list.view()
my_study_list.save_file()
