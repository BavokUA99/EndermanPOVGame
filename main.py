from configs import *

import sys, os

from direct.showbase.ShowBase import ShowBase
from direct.task import Task 

from generation import WorldGeneration
#from player import Player

class MainApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)

		self.worlGeneration = WorldGeneration(self)
		#self.playerA = Player(self)

		self.worlGeneration.generateWorld(self.createCube)

		self.disableMouse()

		self.accept('escape', sys.exit)
		base.buttonThrowers[0].node().setKeystrokeEvent('keystroke')
		self.accept('keystroke', self.keyFunction)   						#from player import Player
		self.taskMgr.add(self.update, "update")                               #from player import Player

		self.mainMoveVector = [0, 0, 0]

		self.camera.setPos(0, 0, 10 * SCALE)

	def createCube(self, x, y, z): #newScale
		#if z > (12 * newScale):
		self.cube = self.loader.loadModel("minecraft_grass_block.glb")
		self.cube.setScale(SCALE, SCALE, SCALE)
		self.cube.setPos(x, y, z)
		self.cube.reparentTo(self.render)
		#else:
		#	self.cube = self.loader.loadModel("minecraft_snow_block.glb")
		#	self.cube.setScale(SCALE, SCALE, SCALE)
		#	self.cube.setPos(x, y, z)
		#	self.cube.reparentTo(self.render)

	def keyFunction(self, keyname):
		if keyname == 'a':
			if self.mainMoveVector[0] > VECTORLIMIT * -1:
				self.mainMoveVector[0] -= VECTORSPEED
		elif keyname == 'd':
			if self.mainMoveVector[0] < VECTORLIMIT:
				self.mainMoveVector[0] += VECTORSPEED
		elif keyname == 'r':
			self.mainMoveVector[2] += VECTORSPEED
		elif keyname == 'f':
			self.mainMoveVector[2] -= VECTORSPEED
		elif keyname == 'w':
			if self.mainMoveVector[1] < VECTORLIMIT:
				self.mainMoveVector[1] += VECTORSPEED
		elif keyname == 's':
			if self.mainMoveVector[1] > VECTORLIMIT * -1:
				self.mainMoveVector[1] -= VECTORSPEED
		elif keyname == 'q':
			pass
		elif keyname == 'e':
			pass

	def calcDronPosition(self):
		X = self.camera.getX() + self.mainMoveVector[0] * MOVESPEED
		Y = self.camera.getY() + self.mainMoveVector[1] * MOVESPEED
		Z = self.camera.getZ() + self.mainMoveVector[2] * MOVESPEED

		#if self.camera.getX() < -58 or self.camera.getX() > 65 or self.camera.getY() > 49 or self.camera.getY() < -73:
		#	self.getChunk(noise)

		self.camera.setPos(X, Y, Z)

		#print((-90 * self.mainMoveVector[1]) / VECTORLIMIT, self.mainMoveVector[1])

		# print(self.mainMoveVector)
		# print(self.camera.getX(), self.camera.getY(), self.camera.getZ())


	def update(self, task):
		self.calcDronPosition()
		md1 = self.win.getPointer(0)

		HprX = 0
		HprY = 0
		HprZ = 0

		HprX = (md1.getX() - 959) * -180 / 959
		HprY = (md1.getY() - 504) * -90 / 504

		self.camera.setHpr(HprX, HprY, HprZ)

		return task.cont

	
if __name__ == '__main__':
	mainApp = MainApp()
	mainApp.run()
