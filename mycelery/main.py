import os
from celery import Celery

# 创建celery实例对象
app = Celery("novel_writer")

# 把celery和django进行组合，识别和加载django的配置文件
if not os.getenv('DJANGO_SETTINGS_MODULE') or \
    os.getenv('DJANGO_SETTINGS_MODULE') == 'novel_writer.settings':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novel_writer.settings')

# 通过app对象加载配置
app.config_from_object("mycelery.config")

# 或者：使用 Django 的 settings 作为 Celery 的配置
# app.config_from_object('django.conf:settings', namespace='CELERY')


# 加载任务
# - 参数必须必须是一个列表，里面的每一个任务都是任务的路径名称
# - 需要启动哪个模块下，则加入列表中
# - app.autodiscover_tasks(["任务1","任务2"])
app.autodiscover_tasks(["mycelery.tasks",])

# 或者：使用自动发现任务
# app.autodiscover_tasks()


# 启动Celery的命令


# 示例1
# 强烈建议切换目录到mycelery根目录下启动
# celery -A mycelery.main worker --loglevel=info
 

# 示例2：
# celery -A NovelCrewAIAgents worker --loglevel=info -Q manager,expert,senior_worker,junior_worker_1,junior_worker_2


# 示例3：
# 单独对一个任务启动命令 会启动指定queue
# celery -A celery_tasks.main  worker -l info -n workerA.%h -Q appone_add_queue
# celery -A celery_tasks.main  worker -l info -n workerB.%h -Q apptwo_mult_queue

# 当任务没有指定queue 则任务会加入default 队列 beat(定时任务也会加入default队列)
# celery -A celery_tasks.main  worker -l info -n worker -Q celery

# 启动定时任务
# celery beat -A celery_tasks.main -l INFO



# 参数说明：
# -A：指定项目名，即mycelery.main，表示项目名是mycelery，启动文件是main.py

# worker：启动worker进程，不加该参数，只启动beat进程
    # worker进程：用于执行任务，每个worker进程对应一个CPU核
    # beat进程：用于定时任务，每分钟执行一次

# --loglevel=info：设置日志级别，可选值有debug、info、warning、error、critical，默认是info
# -Q：指定队列，多个队列用逗号隔开，不加该参数，默认是celery队列
    # celery：默认队列，所有任务都会进入该队列
    # manager：高级员工的任务队列，自定义的任务队列
    # expert：专家任务的队列，自定义的任务队列

# 启动多个worker进程，每个worker进程对应一个队列，每个队列对应一个任务，每个任务对应一个任务函数


# -A 表示 应用目录  这里是celery_tasks.main
# -B 表示 定时任务
# -l 表示日志级别
# -n woker名
# -Q 队列名
# .%h 对应不同主机ip  如果默认localhost，所以可以省略.%h