#!/usr/bin/env python
# -*- coding:utf-8 -*-


SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
            }


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    """
    Convert a file size to human-readable form.
    :param size:file size in bytes
    :param a_kilobyte_is_1024_bytes:if True (default),use multiple of 1024
    :return:string
    """
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
    print(approximate_size(10000000, False))
    print(approximate_size(10000000))



