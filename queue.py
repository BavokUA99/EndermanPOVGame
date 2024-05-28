import time
import threading

class Queue:

	__threadsArray = []
	__MAX_THREADS = 10

	def add(self, element): self.__threadsArray.append(element)

	def remove(self, element): self.__threadsArray.remove(element)

	def start(self):
		self.threadsCount = 0

		for funcIndex in range(len(self.__threadsArray)):

			while True:
				if self.threadsCount + 1 > self.__MAX_THREADS:
					time.sleep(0.2)

				else:
					th = threading.Thread(
							target=self.threadFunc,
							args=(funcIndex,)
						)
					th.start()

					print("Thread has been started")
					self.threadsCount += 1

					break

		print('finish')

	def threadFunc(self, funcIndex:int):
		self.__threadsArray[funcIndex]()

		self.threadsCount -= 1