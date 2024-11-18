from celery import shared_task

@shared_task
def manager_task():
    # 这里是总负责人的任务逻辑
    msg = "Manager task is running"
    print(msg)
    return msg