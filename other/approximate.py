#!/usr/bin/env python
# -*- coding:utf-8 -*-


SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
            }


def approximate(size, a_kilobyte_is_1024_bytes= True):
    if size < 0:
        raise ValueError('number must be no-negative')
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            # return '{0:.1f} {1}'.format(size, suffix)
            return '%.1f %s' % (size, suffix)
    raise ValueError('number too large')


if __name__ == '__main__':
    print(approximate(10000000, False))
    print(approximate(10000000))
