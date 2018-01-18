#!/usr/bin/env bash

# start in different terminals
# no queue tasks
celery -A main worker -l info
# high priority queue
celery -A main worker -l info -Q high
# default priority queue
celery -A main worker -l info -Q default
# low priority queue
celery -A main worker -l info -Q low

# celery beat service
celery -A main worker -l info -B
