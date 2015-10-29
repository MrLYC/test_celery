#!/usr/bin/env python
# encoding: utf-8

import time
from datetime import timedelta, datetime

from .celery_app import DefaultApp

app = DefaultApp(
    __name__,
    borker="redis://localhost",
    backend="rpc://",
)


@app.task(bind=True)
def return_self(self, dl=1):
    time.sleep(dl)
    return self


@app.periodic_task(timedelta(seconds=3), bind=True)
def print_time(self):
    print datetime.now()
