# coding: utf-8

from datetime import datetime


def log_info(s):
    print('{} [Info] {}'.format(datetime.now(), s))


def log_warning(s):
    print('{} [Warning] {}'.format(datetime.now(), s))


def log_error(s):
    print('{} [Error] {}'.format(datetime.now(), s))
