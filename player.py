from configs import *

class Player:
	def __init__(self, ParentClass):
		self = ParentClass

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

	def calcDronPosition(self, task):
		X = self.camera.getX() + self.mainMoveVector[0] * MOVESPEED
		Y = self.camera.getY() + self.mainMoveVector[1] * MOVESPEED
		Z = self.camera.getZ() + self.mainMoveVector[2] * MOVESPEED

		#if self.camera.getX() < -58 or self.camera.getX() > 65 or self.camera.getY() > 49 or self.camera.getY() < -73:
		#	self.getChunk(noise)

		self.camera.setPos(X, Y, Z)

		#HprZ = (-90 * self.mainMoveVector[0]) / VECTORLIMIT
		#HprY = (-90 * self.mainMoveVector[1]) / VECTORLIMIT
		#HprX = 0
		#self.camera.setHpr(HprX, HprY, HprZ)

		print((-90 * self.mainMoveVector[1]) / VECTORLIMIT, self.mainMoveVector[1])

		# print(self.mainMoveVector)
		# print(self.camera.getX(), self.camera.getY(), self.camera.getZ())

		return task.cont