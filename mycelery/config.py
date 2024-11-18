import datetime
import crontab

broker_url = 'redis://127.0.0.1:6379/1'
result_backend = 'redis://127.0.0.1:6379/2'


# Celery 配置
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Redis 作为消息代理
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # 结果存储
CELERY_ACCEPT_CONTENT = ['json']  # 指定消息格式，即使用json格式作为消息格式
CELERY_TASK_SERIALIZER = 'json'   # 指定任务序列化方式
CELERY_RESULT_SERIALIZER = 'json' # 指定结果序列化方式
CELERY_TIMEZONE = 'Asia/Shanghai' # 'UTC' # 时区: UTC是世界标准时间，和北京时间差8小时，建议使用北京时区：'Asia/Shanghai'
# CELERY_ENABLE_UTC = True          # 使用 UTC 时间作为celery的时区

# 为每个智能体创建独立的任务队列
CELERY_QUEUES = {
    'manager': {
        'exchange': 'manager',      # 队列名
        'exchange_type': 'direct',
        'routing_key': 'manager',   # 绑定的routing_key
    },
    'expert': {
        'exchange': 'expert',
        'exchange_type': 'direct',
        'routing_key': 'expert',
    },
    'senior_worker': {
        'exchange': 'senior_worker',
        'exchange_type': 'direct',
        'routing_key': 'senior_worker',
    },
    'junior_worker_for_expert': {
        'exchange': 'junior_worker_for_expert',
        'exchange_type': 'direct',
        'routing_key': 'junior_worker_for_expert',
    },
    'junior_worker_for_senior': {
        'exchange': 'junior_worker_for_senior',
        'exchange_type': 'direct',
        'routing_key': 'junior_worker_for_senior',
    },
}

# 路由
CELERY_ROUTES = {
    'manager': {                  # 这是router 的别名，可以随意定义
        "queue": "manager",       # 指定队列名
        "routing_key": "manager"  # 指定routing_key
        },
    'expert': {
        "queue": "expert",
        "routing_key": "expert"
    },
}

# 为每个任务指定队列
CELERY_ROUTES = {
    'mycelery.tasks.manager_task.*': {
        'queue': 'manager',
        'routing_key': 'manager'
    },
    'mycelery.tasks.expert_task.*': {
        'queue': 'expert',
        'routing_key': 'expert'
    },
    'mycelery.tasks.senior_worker_task.*': {
        'queue': 'senior_worker',
        'routing_key': 'senior_worker'
    },
    'mycelery.tasks.junior_worker_for_expert_task.*': {
        'queue': 'junior_worker_for_expert',
        'routing_key': 'junior_worker_for_expert'
    },
    'mycelery.tasks.junior_worker_for_senior_task.*': {
        'queue': 'junior_worker_for_senior',
        'routing_key': 'junior_worker_for_senior'
    },
}


# # 定时任务配置如下
# CELERYBEAT_SCHEDULE = {
#     'beat_task1': {                                 # 任务名称
#         'task': 'appthree_comment',                 # 方法名称，task_xx.py中的方法名
#         'schedule': datetime.timedelta(seconds=2),  # 间隔时间，方式1：每2秒执行一次
#         'args': (2, 8)                              # 方法参数
#     },
#     'beat_task2': {
#         'task': 'appthree_comment',
#         'schedule': crontab(hour=16, minute=32),    # 方式2：crontab定时任务，表示每日16:32执行
#         'args': (4, 5)
#     },
#     'taskA_schedule' : {
#         'task':'tasks.taskA',
#         'schedule':20,                              # 方式3：每20秒执行一次
#         'args':(5,6)
#     },
# }

