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
import logging

if __name__ == '__main__':
	sys.path.append(r'./../util')
else:
	sys.path.appedn(r'./util')

from myDict import Dict


class DbError(Exception):
	pass


class _Engine(object):
	def __init__(self, connect):
		self._connect = connect

	def connect(self):
		return self._connect()

#database engine singleton holding the MySQldb.connect
engine = None

def create_engine(user, passwd, database, host='127.0.0.1', port=3306, **kw):
	import MySQLdb
	global engine
	if engine is not None:
		raise DbError('RE-initialize of db Engine!')
	params = dict(	user=user, passwd=passwd, database=database, host=host, port=port, buffered=True
					use_unicode=True, charset='utf8', collation='utf8_general_ci', autocommit=False)
	params.update(kw)
	engine = _Engine(lambda: MySQLdb.connect(**params))
	logging.info('Init mysql engine <%s> complete.' % hex(id(engine)))


class _mConnection(object):
	def __init__(self):
		self.connection = None

	def cursor(self):
		if self.connection is None:
			connect_instance = engine.connect()
			logging.info('open connection <%s>' % hex(id(connect_instance)))
			self.connection = connection
		return 

	def commit(self):
		self.connection.commit()
		
	def rollback(self):
		self.connection.rollback()

	def clean_up(self):
		if self.connection:
			connect_instance = self.connection
			self.connection = None
			logging.info('close connection <%s>' % hex(id(connect_instance)))
			connect_instance.close()


class _DbContext(thrading.local):
	def __init__(self):
		self.connection = None
		self.transaction = 0

	def is_init(self):
		return self.connection is not None

	def init(self):
		self.conncetion = _

		


def test():
    mydic = Dict((1, 2, 3), (4, 5, 6))
    print mydic

if __name__ == '__main__':
	test()