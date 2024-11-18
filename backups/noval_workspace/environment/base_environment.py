 # environment/base_environment.py
# from communication.redis_communicator import RedisCommunicator
# 导入celery 的app,以管理celery任务
from mycelery.main import app

class BaseEnvironment:
    """ 模拟办公环境 
    
    功能是将agent整合到一个关键中，方便进行agent的通信，以及任务的分配等。
    实现：
    1. 存储agents，方便进行任务的分配等。
    2. 提供一个send_message和receive_message方法，用于agents之间的通信。
    """
    def __init__(self):
        self.agents = {}
        self.celery_app = app
        # redis的通信模块，暂时弃用，使用celery
        # self.communicator = RedisCommunicator()

    def add_agent(self, agent_id, agent):
        """ 添加一个agent到环境中，并设置其environment为当前环境 """
        if agent_id in self.agents:
            raise ValueError(f"Agent with ID {agent_id} already exists")
        self.agents[agent_id] = agent
        agent.environment = self

    def remove_agent(self, agent_id):
        """ 从环境中移除一个agent """
        if agent_id not in self.agents:
            raise ValueError(f"Agent with ID {agent_id} does not exist")
        del self.agents[agent_id]

    def get_agent(self, agent_id):
        """ 获取一个agent """
        return self.agents.get(agent_id)

    def list_agents(self, list_name=False):
        """ 获取环境中的所有agent的id，或name """
        if list_name:
            return [agent.name for agent in self.agents.values()] 
        return list(self.agents.keys()) 
    
    def send_message(self, sender_id, receiver_id, content):
        if receiver_id not in self.agents:
            raise ValueError(f"Receiver with ID {receiver_id} does not exist")
        
        message = {
            "sender_id": self.id,
            "receiver_id": receiver_id,
            "content": content
        }
        self.communicator.send_message(sender_id, receiver_id, message)

    def receive_message(self, agent_id):
        return self.communicator.receive_message(agent_id)
    
    def run(self):
        raise NotImplementedError("Subclasses must implement the run method")