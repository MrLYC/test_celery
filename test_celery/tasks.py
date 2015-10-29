#!/usr/bin/env python
# encoding: utf-8

import time

from celery import Celery

app = Celery(
    __name__,
    borker="redis://localhost",
    backend="rpc://",
)


@app.task(bind=True)
def return_self(self, dl=1):
    time.sleep(dl)
    return self
