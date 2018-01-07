from celery import task, shared_task
import time



@task()
def task_number1():
    print('EXECUTE TASK 1')
    time.sleep(2)

@shared_task
def task_number2():
    print('EXECUTE TASK 2')
    time.sleep(2)

@shared_task
def task_number3():
    print('EXECUTE TASK 3')
    time.sleep(2)
