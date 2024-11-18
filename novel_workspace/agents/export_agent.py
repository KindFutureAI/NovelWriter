from worker_agent import WorkerAgent
from tasks.task_manager import TaskManager 
from ..utils.config import nw_config

class ExportAgent(WorkerAgent):
    name = nw_config.AGENTS['Export']['name']
    level = nw_config.AGENTS['Export']['level']
    def __init__(self, nick_name=None):
        super().__init__()
        self.nick_name = nick_name
    def _init(self):

        self.task_manager = TaskManager()

 
    def run(self):
        pass        