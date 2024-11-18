import uuid
from .task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def create_task(self, name, status="WAITING", description="", prompt=""):
        """ 创建新的任务 """
        task_id = str(uuid.uuid4())
        task = Task(
            task_id, 
            name,
            status=status,
            description=description, 
            prompt=prompt,
        )
        self.tasks[name] = task

    def get_task(self, name):
        """ 获取任务详情 """
        return self.tasks.get(name)

    def update_task_status(self, task_id, status):
        """ 更新任务的状态 """
        if task_id in self.tasks:
            self.tasks[task_id].status = status
        else:
            raise ValueError(f"Task with ID {task_id} not found")

    def process_task(self, task):
        print(f"                Processing task...{task.name}  Done!!!")

    def list_tasks(self):
        """ 列出所有任务 """
        return [task.to_dict() for task in self.tasks.values()]

    def __str__(self):
        """ 返回所有任务的字符串表示 """
        if not self.tasks:
            return "No tasks available"
        
        task_strings = [str(task) for task in self.tasks.values()]
        return "\n\n".join(task_strings)  # 使用两个换行符分隔每个任务，使输出更易读 