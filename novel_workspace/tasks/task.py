class Task:
    """
    任务类，用于描述一个任务的类型、内容、状态等属性。
    
    :param task_id: 任务ID
    :param name: 任务类型, 例如：writing, editing, character_development, plot_generation, idea_input, feedback
    :param prompt: 提示词，用于描述任务的要求和目标
    :param description: 任务内容
    :param status: 任务状态, 默认为"WAITING"
    """
    def __init__(self, task_id, name, description, prompt, status):
        self.task_id = task_id 
        self.name = name     
        self.status = status  # WAITING, IN_PROGRESS, COMPLETED, FAILED
        self.prompt = prompt 
        self.description = description

    def to_dict(self):
        # 将Task对象转换为字典
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, task_dict):
        # 从字典中创建一个Task对象
        return cls(
            task_id=task_dict["task_id"],
            name=task_dict["name"],
            description=task_dict["description"],
            status=task_dict["status"]
        )

    def __str__(self):
        return f"Task ID: {self.task_id}, Type: {self.name}, Status: {self.status}, description: {self.description}"