from celery import shared_task as task
import time

############################################################
# USE DECORATOR ARGUMENT queue IF SETTINGS ROUTING NOT WORKS
############################################################


@task(queue='default')
def task_number1():
    print('EXECUTE TASK 1 default')
    time.sleep(2)


@task(queue='high')
def task_number2():
    print('EXECUTE TASK 2 high')
    time.sleep(2)


@task(queue='low')
def task_number3():
    print('EXECUTE TASK 3 low')
    time.sleep(2)


@task(queue='low')
def task_number4():
    print('EXECUTE TASK 4 low')
    time.sleep(2)


@task(queue='low')
def task_number5():
    print('EXECUTE TASK 5 scheduled')
    time.sleep(2)
