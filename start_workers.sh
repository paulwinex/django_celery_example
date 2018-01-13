
# start in different terminals
# high priority queue
celery -A main worker -l info -Q high
# default priority queue
celery -A main worker -l info -Q default
# low priority queue
celery -A main worker -l info -Q low
# celery beat service
celery -A main worker -l info -B
