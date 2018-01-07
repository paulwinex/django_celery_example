
# start in different terminals
celery -A main worker -l info -Q high

celery -A main worker -l info -Q normal
