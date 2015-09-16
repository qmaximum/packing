# -*- coding: utf-8 -*-

__author__ = 'qmax'


# 一条代码 code qty l路由串
class PackItem():
	def __init__(self, code, qty, route):
		self.code = code
		self.qty = qty
		self.route = route
		self.nextloc = self.getnextloc()

	def getnextloc(self):
		if len(self.route) >= 1:
			return self.rout.pop()
		else:
			return None

	def updateroute(self):
		self.nextloc = self.getnextloc()


# 一个包或者袋视为虚拟包，以包号为key,#作为袋的默认包号
class WorkPack():
	def __init__(self, packno='#'):
		self.packno = packno
		self.packsum = 0
		self.packqty = 0
		self.pack = []
		self.nextloc = ''
		if packno == '#':
			self.ispack = False
		else:
			self.ispack = True

	def additem(self, packitem):
		if self.nextloc == '':
			self.nextloc = packitem.nextloc
		elif self.nextloc != packitem.nextloc:
			raise 'wrong loc and wt info!!'
		self.pack.append(packitem)
		self.packqty += packitem.qty
		self.packsum += 1

	def popitem(self):
		if self.packsum < 1:
			return None
		else:
			tempitem = self.pack.pop()
			self.packsum -= 1
			self.packqty -= tempitem.qty
			return tempitem

	def updateroute(self):
		self.nextloc = self.pack[0].nextloc


# 总的资源包，以场地班次为key
class WorkLoad():
	def __init__(self, locwt=''):
		self.key = locwt
		self.load = []
		self.sum = 0

	def addpack(self, workpack):
		if self.key == '':
			self.key = workpack.nextloc
		elif self.key != workpack.nextloc:
			raise 'wrong loc and wt info!!'
		self.load.append(workpack)
		self.sum += 1

	def poppack(self):
		if self.sum < 1:
			return None
		else:
			self.sum -= 1
			return self.load.pop()

