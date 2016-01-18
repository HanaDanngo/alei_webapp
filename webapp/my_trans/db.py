#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Danngo Alei'

'''
light weigt database operation module.
'''

import sys
import time
import functools
import threading

sys.path.append('./../util')
from myDict import Dict





def test():
    mydic = Dict((1, 2, 3), (4, 5, 6))
    print mydic


if __name__ == '__main__':
    test()