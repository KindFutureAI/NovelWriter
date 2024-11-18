import os
import yaml


current_dir = os.path.dirname(__file__)
config_file = os.path.join(current_dir, 'assets', 'config.yaml')
tasks_file = os.path.join(current_dir, 'assets', 'tasks.yaml')

# TODO 等项目demo运行起来之后，就将这个大的配置文件拆分成更小的配置文件，方便管理
ROLE_TYPES = {
    'manager': 'manager',
    'worker': 'worker'
}

TASKS = {
    'idea_input': {
        'name': 'idea_input',
        'description': '提供创意',
        'prompt':"",
        'status': 'WAITING'
    },
    'plot_generation': {
        'name': 'plot_generation',
        'description': '生成故事情节',
        'prompt':"",
        'status': 'WAITING'
    },
    'character_development': {
        'name': 'character_development',
        'description': '开发角色',
        'prompt':"",
        'status': 'WAITING'
    },
    'writing': {
        'name': 'writing',
        'description': '撰写故事',
        'prompt':"",
        'status': 'WAITING'
    },
    'editing': {
        'name': 'editing',
        'description': '编辑和校对',
        'prompt':"",
        'status': 'WAITING'
    },
    'reading_simulation': {
        'name': 'reading_simulation',
        'description': '模拟读者反馈',
        'prompt':"",
        'status': 'WAITING'
    }
}


ROLES = { 
    'IdeaInputer': {
        'name': 'IdeaInputer',
        'tasks': [
            TASKS['idea_input']
        ],
        'description': '负责提供创意'
    },
    'PlotGenerator': {
        'name': 'PlotGenerator',
        'tasks': [
            TASKS['plot_generation']
        ],
        'description': '负责生成故事情节'
    },
    'CharacterDeveloper': {
        'name': 'CharacterDeveloper',
        'tasks': [
            TASKS['character_development']
        ],
        'description': '负责开发角色'
    },
    'Writer': {
        'name': 'Writer',
        'tasks': [
            TASKS['writing']
        ],
        'description': '负责撰写故事'
    },
    'Editor': {
        'name': 'Editor',
        'tasks': [
            TASKS['editing']
        ],
        'description': '负责编辑和校对'
    },
    'ReaderSimulator': {
        'name': 'ReaderSimulator',
        'tasks': [
            TASKS['reading_simulation']
        ],
        'description': '模拟读者反馈'
    }
}

AGENTS = {  
    'Manager': {
        'name': 'Manager',
        'nick_name': '老板',
        'type': ROLE_TYPES['manager'],
        'level': 1,
        'roles': [ROLES['IdeaInputer'],
                  ROLES['PlotGenerator'],
                  ROLES['CharacterDeveloper'],
                  ROLES['Writer'],
                  ROLES['Editor'],
                  ROLES['ReaderSimulator']
                  ],
        'status': 'FREE',
        'description': '总负责人，负责整个项目的规划和整理'
    },
    'Expert': {
        'name': 'Expert',
        'nick_name': '阿娟',
        'type': ROLE_TYPES['worker'],
        'level': 2,
        'roles': [ROLES['IdeaInputer'],
                  ROLES['PlotGenerator'],
                  ROLES['CharacterDeveloper'],
                  ROLES['Writer'],
                  ROLES['Editor'],
                  ROLES['ReaderSimulator']
                  ],
        'status': 'FREE',
        'description': '专家，与初级员工组成一个业务小组'
    },
    'Senior': {
        'name': 'Senior',
        'nick_name': '翠翠',
        'type': ROLE_TYPES['worker'],
        'level': 3,
        'roles': [ROLES['IdeaInputer'],
                  ROLES['PlotGenerator'],
                  ROLES['CharacterDeveloper'],
                  ROLES['Writer'],
                  ROLES['Editor'] 
                  ],
        'status': 'FREE',
        'description': '高级职位员工，与初级员工组成一个业务小组'
    },
    'JuniorForExpert': {
        'name': 'JuniorForExpert',
        'nick_name': '铁柱',
        'type': ROLE_TYPES['worker'],
        'level': 4,
        'roles': [ROLES['IdeaInputer'],
                  ROLES['PlotGenerator'],
                  ROLES['CharacterDeveloper'],
                  ROLES['Writer']  
                  ],
        'status': 'FREE',
        'description': '初级员工，负责专家小组的任务'
    },
    'JuniorForSenior': {
        'name': 'JuniorForSenior',
        'nick_name': '吴琴',
        'type': ROLE_TYPES['worker'],
        'level': 4,
        'roles': [ROLES['IdeaInputer'],
                  ROLES['PlotGenerator'],
                  ROLES['CharacterDeveloper'],
                  ROLES['Writer'] 
                  ],
        'status': 'FREE',
        'description': '初级员工，负责高级职位员工小组的任务'
    }
}

class NWConfig:
    NOVEL_WORKSPACE_CONFIG = {}
    NOVEL_WORKSPACE_CONFIG_PATH = config_file
    TASKS_FILE_PATH = tasks_file

    TASKS = TASKS
    ROLES = ROLES
    AGENTS = AGENTS

    def __init__(self):
        self.update_tasks()

    def update_tasks(self):
        """ 更新 tasks ：从文件中读取任务 """
        with open(self.TASKS_FILE_PATH, 'r') as f:
            tasks = yaml.safe_load(f)
            if not tasks:
                return 

            # 将新的任务，从配置文件中添加到字典中
            for task in tasks:
                if task not in self.TASKS:
                    self.TASKS[task] = tasks[task]
    
    def save_tasks(self, task_name, description=""):
        """ 将任务保存到文件中 """
        if task_name in self.TASKS:
            print(f"任务 {task_name} 已经存在，无法保存")
            return

        new_task = {task_name: {'name': task_name, 'description': description}}
        # 需要将这个 new_task 加入到 tasks 文件的末尾：
        with open(self.TASKS_FILE_PATH, 'a', encoding="utf-8") as f:
            yaml.dump(new_task, f, allow_unicode=True)
        
        self.TASKS[task_name] = new_task[task_name]
        



nw_config = NWConfig()

if __name__ == '__main__':
    print(nw_config.TASKS)
    nw_config.save_tasks('test_task2', '这是一个测试任务')
    print(nw_config.TASKS)
 