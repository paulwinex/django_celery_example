from core import tasks
from datetime import timedelta, datetime

# call tasks for specific queue defined if decorator
tasks.task_default.delay()
tasks.task_high.delay()
tasks.task_low.delay()
tasks.task_no_queue.delay()

# change default queue
tasks.task_high.apply_async(queue='default')
tasks.task_default.apply_async(queue='high')
tasks.task_default.apply_async(queue='low')
# start class static method as task
tasks.Tasks.task_inside_class.delay()

# start task with countdown (task_no_queue will be executed first
tasks.task_with_countdown.delay()
tasks.task_no_queue.delay()
# schedule task to specific time with datetime
tasks.task_no_queue.apply_async(eta=datetime.now()+timedelta(seconds=3))
# add countdown for any task
tasks.task_no_queue.apply_async(countdown=4)

# try to execute task 2 times and do something other if not works
tasks.task_retry.delay()


