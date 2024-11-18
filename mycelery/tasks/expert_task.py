from celery import shared_task
from mycelery.main import app

# 定义一个共享的任务
# @shared_task
# def expert_task():
#     """
#     运行时，celery会自动识别这个任务
#     shared_task: 将函数注册为 celery 任务
#     """
#     # 这里是专家的任务逻辑
#     print("Expert task is running")

@app.task(name='expert')
def expert_task():
    """
    使用 app.task 注册任务，将函数注册为 celery 任务
    使用 name 参数指定任务名称，会将这个函数注册为名为 expert 的任务
    """
    # 这里是专家的任务逻辑
    msg = "Expert task is running"
    print(msg)
    return msg