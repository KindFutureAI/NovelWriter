import uuid
from .base_agent import BaseAgent 

class AgentManager:

    def __init__(self): 
        self.agents = {}
    
    def create_agent(self, name, nick_name=None, type='Worker', level=4, roles=[], status='FREE', description=""):
        """ Create an agent """
        agent_id = str(uuid.uuid4())
        agent = BaseAgent(
            agent_id, 
            name, 
            nick_name=nick_name if nick_name else name,
            type=type, 
            level=level, 
            roles=roles,
            status=status,
            description=description,
        )
        self.agents[name] = agent

    def list_agents(self):
        """ List all agents """
        return [agent for agent in self.agents.values()]
 
    def run(self):
        pass        