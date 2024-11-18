from .worker_agent import WorkerAgent
from ..utils.config import nw_config

class JuniorForSeniorAgent(WorkerAgent):
    name = nw_config.AGENTS['JuniorForSenior']['name']
    level = nw_config.AGENTS['JuniorForSenior']['level'] 
    def __init__(self, nick_name=None):
        super().__init__()
        self.nick_name = nick_name
    def _init(self):

        pass

 
    def run(self):
        pass        