#!/usr/bin/env python
# encoding: utf-8

from celery import Celery


class DefaultApp(Celery):
    DEFAULT_CONF = dict(
        CELERY_TIMEZONE="Asia/Shanghai",
        CELERYBEAT_SCHEDULE={},
    )

    def __init__(self, *args, **kwargs):
        super(DefaultApp, self).__init__(*args, **kwargs)
        self.conf.update(self.DEFAULT_CONF)

    def periodic_task(self, schedule, args=(), **kwargs):
        def wrapper(f):
            func = self.task(f, **kwargs)
            self.conf.CELERYBEAT_SCHEDULE[func.name] = {
                "task": func.name,
                "schedule": schedule,
                "args": args,
            }
            return func
        return wrapper
