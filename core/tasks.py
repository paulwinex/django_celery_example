from celery import shared_task as task
import time

############################################################
# USE DECORATOR ARGUMENT queue IF SETTINGS ROUTING NOT WORKS
############################################################


@task(queue='default')
def task_default():
    print('EXECUTE TASK default')
    time.sleep(2)


@task(queue='high')
def task_high():
    print('EXECUTE TASK high')
    time.sleep(2)


@task(queue='low')
def task_low():
    print('EXECUTE TASK low')
    time.sleep(2)


@task(queue='low')
def task_scheduled():
    print('EXECUTE TASK scheduled')
    time.sleep(2)

@task
def task_no_queue():
    print('EXECUTE TASK no queue and go to default')
    time.sleep(2)


@task(countdown=5)
def task_with_countdown():
    print('EXECUTE TASK with countdown')
    time.sleep(2)


@task(bind=True)
def task_raise_and_retry(self):
    print('EXECUTE TASK error and retry 2 times with countdown 3 sec')
    try:
        raise Exception('Test error')
    except Exception as e:
        self.retry(countdown=3, exc=e, max_retries=2)


@task
def task_error():
    raise Exception('ERROR')


@task(bind=True)
def task_retry(self):
    retries = 2
    print('>>> TRY #%s' % self.request.retries)
    if self.request.retries == retries:
        print('It was last try, do something other')
        other_way.delay()
        return
    self.retry(countdown=3, max_retries=retries)
@task
def other_way():
    print('Other way...')


@task(bind=True)
def task_request(self):
    for k, v in self.request.__dict__.items():
        print('{} : {}'.format(k, v))


class Tasks(object):
    @staticmethod
    @task
    def task_inside_class():
        print('HELLO FROM CLASS METHOD')
