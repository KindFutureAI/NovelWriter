class Role:
    def __init__(self,role_id, name, description, tasks):

        # 基础属性
        self.role_id = role_id
        self.name = name                # 职位角色名称
        self.description = description  # 职位角色描述
        self.tasks = tasks              # 职位任务列表 


    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        self.tasks.remove(task)
    

    # ——————————————————————————————————————————————————————————————————————————
    # 下面是一些辅助方法
    # ——————————————————————————————————————————————————————————————————————————


    def __str__(self):
        return f"Role: {self.name}"