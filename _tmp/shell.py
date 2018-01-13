from core import tasks

# call tasks for specific queue defined if decorator
tasks.task_number1.delay()
tasks.task_number2.delay()
tasks.task_number3.delay()
tasks.task_number4.delay()
tasks.task_number5.delay()

# change default queue
tasks.task_number1.apply_async(queue='default')
tasks.task_number1.apply_async(queue='high')
tasks.task_number1.apply_async(queue='low')

