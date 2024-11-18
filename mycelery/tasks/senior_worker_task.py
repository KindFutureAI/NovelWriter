from celery import shared_task

@shared_task
def senior_worker_task():
    # 这里是高级员工的任务逻辑
    msg = "Senior worker task is running"
    print(msg)
    return msg