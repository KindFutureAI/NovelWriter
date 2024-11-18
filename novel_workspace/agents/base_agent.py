class BaseAgent:
    """ 团队成员基类 
    
    类功能：
    1. 记录成员信息：包括ID，名称，职位级别，任务等
    2. 职位角色管理：添加、移除角色
    3. 职位消息管理：发送、接收消息
    """
    def __init__(self, agent_id, name, type, nick_name, level, roles, status, description):
        # 基础信息
        self.agent_id = agent_id        # ID
        self.name = name                # 名称
        self.type = type                # 职位分类: MANAGER, WORKER
        self.level = level              # 职位级别: 1-5
        self.nick_name = nick_name if nick_name else name       # 自定义的昵称
        self.status = status
        self.description = description

        # 成员的岗位角色信息
        self.roles = roles              # 角色 
 

        # 成员的状态信息，如：是否空闲、待办任务
        self.is_free = True             # 是否空闲
        self.task_board = []            # 待办任务列表

    def add_role(self, role):
        """ 添加角色：一个agent 可以有多个角色 """
        self.roles.append(role)
        
    def remove_role(self, role):
        """ 移除角色 """
        self.roles.remove(role)

    def get_role(self, role_name):
        """ 获取角色 """
        for role in self.roles:
            if role.name == role_name:
                return role
     
    # ——————————————————————————————————————————————————————————————————————————
    # 消息相关方法
    # ——————————————————————————————————————————————————————————————————————————

    def send_message(self, receiver_id, content):
        """ 发送消息 """
        message = {
            "sender_id": self.id,
            "receiver_id": receiver_id,
            "content": content
        }
        self.environment.communicator.send_message(message)

    def receive_message(self, message):
        """ 接收消息 """
        if message["receiver_id"] == self.id:
            self.handle_message(message)

    def handle_message(self, message):
        """ 处理消息 """
        raise NotImplementedError("Subclasses must implement this method")

    def report_to_leader(self, leader_id, message):
        # 向 leader_id 报告消息
        self.send_message(leader_id, message) 


    # ——————————————————————————————————————————————————————————————————————————

    # ——————————————————————————————————————————————————————————————————————————
    def run(self):
        """ 运行 """
        raise NotImplementedError("Subclasses must implement this method")
    
 
 

    # ——————————————————————————————————————————————————————————————————————————
    # 状态相关方法  todo
    # ——————————————————————————————————————————————————————————————————————————
 
    def get_status(self):
        """ 获取状态 """
        return self.is_free    
    
    def update_status(self):
        """ 切换状态 """
        if self.is_free:
            self.is_free = False
        else:
            self.is_free = True    

    def check_task_board(self):
        """ 检查待办任务列表 """
        return self.task_board


    def __str__(self):
        """ 输出信息 """
        return f"Agent: {self.name}"        