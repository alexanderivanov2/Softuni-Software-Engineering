class Section():
    def __init__(self, name):
        self.name = name
        self.tasks = {}

    def add_task(self, new_task):
        if new_task.name in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks[new_task.name] = new_task
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name].completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        for_deletion = []
        for task in self.tasks.values():
            if task.completed:
                for_deletion.append(task.name)
        for delete_this in for_deletion:
            self.tasks.pop(delete_this)
        return f"Cleared {len(for_deletion)} tasks."

    def view_section(self):
        first_part = f"Section {self.name}:\n"
        second_part = '\n'.join(el.details() for el in self.tasks.values())
        return first_part + second_part