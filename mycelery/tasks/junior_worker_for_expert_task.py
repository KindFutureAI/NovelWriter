from celery import shared_task

@shared_task
def junior_worker_for_expert_task():
    # 这里是初级员工1的任务逻辑
    msg = "Junior worker(for expert) task is running"
    print(msg)
    return msg