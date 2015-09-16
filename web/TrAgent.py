# -*- coding: utf-8 -*-

__author__ = 'qmax'


import pyodbc
import workpack
from rules import TrRules

transcost  = 1
unpackcost = 1
packcost = 1





class BasicAgent():
	name = 'basicagent'

	def __init__(self, locwt, con, ispoint=True):
		self.locwt = locwt
		self.ispoint = ispoint
		self.r = con
		self.rules = TrRules(locwt)
		self.barnpack = []
		self.barnitem = {}
		self.cost = 0


	# 如果场地是点部，那么需要判断workload是收还是派
	# 泄车前保证本场地无屯货
	def unloadtruck(self, workload):
		assert self.locwt == workload.key

		if self.ispoint and workload.sum == 1 and workload.load[0].packno == '#':  # 收货端
			wp = workload.load[0]
			for item in wp.pack:
				self.barnitem.append(item)
		elif self.ispoint and workload.sum >= 1 and workload.load[0].packno != '#':  # 派送端
			self.cost += transcost
			self.cost += unpackcost
		elif not self.ispoint:  # 中转场
			for wp in workload.load:
				self.barnpack.append(wp)

	def cleanbarn(self):
		self.barnitem = []
		self.barnpack = []

	def loadtruck(self):
		return self.barnpack

	def unpack(self):
		if self.barnpack == []:
			pass
		else:
			tempbarn = []
			for wp in self.barnpack:
				self.cost += transcost
				if self.rules.needunpack(wp):  # 符合拆包条件
					self.cost += unpackcost
					for item in wp.pack:
						item.updateroute()
						self.cost += transcost  # 扫件成本
						if item.code + item.nextloc + item.route in self.barnitem.keys():
							self.barnitem[item.code + item.nextloc + item.route] += item.qty
						else:
							self.barnitem[item.code + item.nextloc + item.route] = item.qty
				else:  #对于不需要拆的包，更新票和包的nextloc
					for item in wp.pack:
						item.updateroute()
					wp.updateroute()
					tempbarn.append(wp)
		self.barnpack = []
		self.barnpack.extend(tempbarn)


	def pack(self):
		pass






