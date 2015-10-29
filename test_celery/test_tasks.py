#!/usr/bin/env python
# encoding: utf-8

from unittest import TestCase

from . import tasks


class TestSimpleTasks(TestCase):
    def setUp(self):
        self._CELERY_ALWAYS_EAGER = tasks.app.conf.CELERY_ALWAYS_EAGER
        tasks.app.conf.CELERY_ALWAYS_EAGER = True

    def tearDown(self):
        tasks.app.conf.CELERY_ALWAYS_EAGER = self._CELERY_ALWAYS_EAGER

    def test_return_self(self):
        result = tasks.return_self.delay(0.1)
        self.assertIsInstance(
            result.get(),
            tasks.return_self.__class__,
        )
