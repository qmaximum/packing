# -*- coding: utf-8 -*-

__author__ = 'qmax'


class PackRule():
	def __init__(self, rulename, packcode):
		self.rulename = rulename
		self.packcode = packcode

class PackRules():
	def __init__(self, filepath):
		self.rules = {}
		with open(filepath) as f:
			for line in f.readlines():
				if line[0] in self.rules.keys():
					print 'duplicate keys'
				else:
					self.rules[line[0]] = line[1]


	def needunpack(self):
		return False


