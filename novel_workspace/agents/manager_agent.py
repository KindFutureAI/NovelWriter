# agents/manager_agent.py
from .base_agent import BaseAgent
from roles.manager_role import ManagerRole
from tasks.task import Task
from tasks.task_manager import TaskManager 
from ..utils.config import nw_config

class ManagerAgent(BaseAgent):
    name = nw_config.AGENTS['Manager']['name']
    level = nw_config.AGENTS['Manager']['level']
    def __init__(self, nick_name=None):
        super().__init__()
        self.nick_name = nick_name
    def _init(self):

        self.task_manager = TaskManager()

 
    def run(self):
        pass        