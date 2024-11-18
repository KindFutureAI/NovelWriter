from tasks.task_manager import TaskManager
from roles.role_manager import RoleManager
from agents.agent_manager import AgentManager
from utils.config import nw_config


def init_tasks(task_manager):
    """ 初始化任务：从配置中载入 """

    # 从配置中获取任务列表，加载到系统中
    for task_name in nw_config.TASKS:
        task_manager.create_task(
            name=nw_config.TASKS[task_name]['name'],
            prompt=nw_config.TASKS[task_name]['prompt'],
            status=nw_config.TASKS[task_name]['status']
        )

    # task_manager.create_task(
    #     name=nw_config.TASKS['idea_input']['name'],
    #     prompt=nw_config.TASKS['idea_input']['prompt'],
    #     status=nw_config.TASKS['idea_input']['status'],
    #     description=nw_config.TASKS['idea_input']['description'],
    # )

    # task_manager.create_task(
    #     name=nw_config.TASKS['plot_generation']['name'],
    #     prompt=nw_config.TASKS['plot_generation']['prompt'],
    #     status=nw_config.TASKS['plot_generation']['status'],
    #     description=nw_config.TASKS['plot_generation']['description'],
    # )

    # task_manager.create_task(
    #     name=nw_config.TASKS['character_development']['name'],
    #     prompt=nw_config.TASKS['character_development']['prompt'],
    #     status=nw_config.TASKS['character_development']['status'],
    #     description=nw_config.TASKS['character_development']['description'],
    # )

    # task_manager.create_task(
    #     name=nw_config.TASKS['writing']['name'],
    #     prompt=nw_config.TASKS['writing']['prompt'],
    #     status=nw_config.TASKS['writing']['status'],
    #     description=nw_config.TASKS['writing']['description'],
    # )

    # task_manager.create_task(
    #     name=nw_config.TASKS['editing']['name'],
    #     prompt=nw_config.TASKS['editing']['prompt'],
    #     status=nw_config.TASKS['editing']['status'],
    #     description=nw_config.TASKS['editing']['description'],
    # )

    # task_manager.create_task(
    #     name=nw_config.TASKS['reading_simulation']['name'],
    #     prompt=nw_config.TASKS['reading_simulation']['prompt'],
    #     status=nw_config.TASKS['reading_simulation']['status'],
    #     description=nw_config.TASKS['reading_simulation']['description'],
    # )

def init_roles(role_manager):    
    """ 初始化工作职责角色：从配置中载入 """

    # 
    for role_name in nw_config.ROLES:
        role_manager.create_role(
            name=nw_config.ROLES[role_name]['name'],
            description=nw_config.ROLES[role_name]['description'],
            tasks=nw_config.ROLES[role_name]['tasks']
        )

    # role_manager.create_role(
    #     name=nw_config.ROLES['IdeaInputer']['name'],
    #     description=nw_config.ROLES['IdeaInputer']['description'],
    #     tasks=nw_config.ROLES['IdeaInputer']['tasks']
    # )

    # role_manager.create_role(
    #     name=nw_config.ROLES['PlotGenerator']['name'],
    #     description=nw_config.ROLES['PlotGenerator']['description'],
    #     tasks=nw_config.ROLES['PlotGenerator']['tasks']
    # )

    # role_manager.create_role(
    #     name=nw_config.ROLES['CharacterDeveloper']['name'],
    #     description=nw_config.ROLES['CharacterDeveloper']['description'],
    #     tasks=nw_config.ROLES['CharacterDeveloper']['tasks']
    # )

    # role_manager.create_role(
    #     name=nw_config.ROLES['Writer']['name'],
    #     description=nw_config.ROLES['Writer']['description'],
    #     tasks=nw_config.ROLES['Writer']['tasks']
    # )

    # role_manager.create_role(
    #     name=nw_config.ROLES['Editor']['name'],
    #     description=nw_config.ROLES['Editor']['description'],
    #     tasks=nw_config.ROLES['Editor']['tasks']
    # )

    # role_manager.create_role(
    #     name=nw_config.ROLES['ReaderSimulator']['name'],
    #     description=nw_config.ROLES['ReaderSimulator']['description'],
    #     tasks=nw_config.ROLES['ReaderSimulator']['tasks']
    # ) 

def init_agents(agent_manager): 
    """ 初始化agents: 从配置中载入 """

    for agent_name in nw_config.AGENTS:
        agent_manager.create_agent(
            name=nw_config.AGENTS[agent_name]['name'], 
            nick_name=nw_config.AGENTS[agent_name]['nick_name'], 
            type=nw_config.AGENTS[agent_name]['type'], 
            level=nw_config.AGENTS[agent_name]['level'], 
            roles=nw_config.AGENTS[agent_name]['roles'], 
            status=nw_config.AGENTS[agent_name]['status'], 
            description=nw_config.AGENTS[agent_name]['description']
        )

    # agent_manager.create_agent(
    #     nw_config.AGENTS['Manager']['name'], 
    #     type=nw_config.AGENTS['Manager']['type'], 
    #     level=nw_config.AGENTS['Manager']['level'], 
    #     roles=nw_config.AGENTS['Manager']['roles'], 
    #     nick_name=nw_config.AGENTS['Manager']['nick_name'],
    #     description=nw_config.AGENTS['Manager']['description']
    # )

    # agent_manager.create_agent(
    #     nw_config.AGENTS['Expert']['name'], 
    #     type=nw_config.AGENTS['Expert']['type'], 
    #     level=nw_config.AGENTS['Expert']['level'], 
    #     roles=nw_config.AGENTS['Expert']['roles'], 
    #     nick_name=nw_config.AGENTS['Expert']['nick_name'],
    #     description=nw_config.AGENTS['Expert']['description']
    # )

    # agent_manager.create_agent(
    #     nw_config.AGENTS['Senior']['name'], 
    #     type=nw_config.AGENTS['Senior']['type'], 
    #     level=nw_config.AGENTS['Senior']['level'], 
    #     roles=nw_config.AGENTS['Senior']['roles'], 
    #     nick_name=nw_config.AGENTS['Senior']['nick_name'],
    #     description=nw_config.AGENTS['Senior']['description']
    # )

    # agent_manager.create_agent(
    #     nw_config.AGENTS['JuniorForExpert']['name'], 
    #     type=nw_config.AGENTS['JuniorForExpert']['type'], 
    #     level=nw_config.AGENTS['JuniorForExpert']['level'], 
    #     roles=nw_config.AGENTS['JuniorForExpert']['roles'], 
    #     nick_name=nw_config.AGENTS['JuniorForExpert']['nick_name'],
    #     description=nw_config.AGENTS['JuniorForExpert']['description']
    # )

    # agent_manager.create_agent(
    #     nw_config.AGENTS['JuniorForSenior']['name'], 
    #     type=nw_config.AGENTS['JuniorForSenior']['type'], 
    #     level=nw_config.AGENTS['JuniorForSenior']['level'], 
    #     roles=nw_config.AGENTS['JuniorForSenior']['roles'], 
    #     nick_name=nw_config.AGENTS['JuniorForSenior']['nick_name'],
    #     description=nw_config.AGENTS['JuniorForSenior']['description']
    # )

def main():
 
    task_manager = TaskManager()  # 工作任务管理工具  
    role_manager = RoleManager()  # 工作岗位管理工具
    agent_manager = AgentManager()

   
    init_tasks(task_manager)  # 初始化任务
    init_roles(role_manager)  # 初始化工作岗位
    init_agents(agent_manager)

    # 模拟测试agent是否可以开始执行任务
    agents = agent_manager.list_agents()
    for agent in agents:
        print(f"{agent.nick_name:<6}, 职位级别: {agent.type:<10}, 职位名称: {agent.name:<10}  状态：{agent.status}")
        for role in agent.roles:
            print(f"    - 当前职责：{role['name']:<10}  {role['description']}")
            for task in role['tasks']:
                print(f"      - 当前任务：{task['name']:<10}  {task['description']}")

                _task = task_manager.get_task(task['name'])
                task_manager.process_task(_task)



if __name__ == "__main__":
    main()