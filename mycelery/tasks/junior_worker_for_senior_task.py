from celery import shared_task
 
@shared_task
def junior_worker_for_senior_task():
    # 这里是初级员工2的任务逻辑
    msg = "Junior worker(for senior) task is running"
    print(msg)
    return msg