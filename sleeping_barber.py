from threading import Thread, Lock, Event
import time, random

mutex = Lock()

#Interval in seconds
cus_min = 5
cus_max = 5
hair_min = 3
hair_max = 5

class shop:
	cus = []

	def __init__(self, barber, n):
		self.barber = barber
		self.n = n

	def openShop(self):
		print ('Barber shop is opening')
		work = Thread(target = self.gowork)
		work.start()

	def gowork(self):
		while True:
			mutex.acquire()

			if len(self.cus) > 0:
				c = self.cus[0]
				del self.cus[0]
				mutex.release()
				self.barber.cutHair(c)
			else:
				mutex.release()
				print ('Aaah, all done, going to sleep')
				barber.sleep()
				print ('Barber woke up')
	
	def enter(self, customer):
		mutex.acquire()
		print ('\n>> {0} entered the shop and is looking for a seat'.format(customer.name))

		if len(self.cus) == self.n:
			print ('\nWaiting room is full, {0} is leaving.'.format(customer.name))
			mutex.release()
		else:
			print ('{0} sat down in the waiting room'.format(customer.name))	
			self.cus.append(c)	
			mutex.release()
			barber.wakeUp()

class Customer:
	def __init__(self, name):
		self.name = name

class Barber:
	work = Event()

	def sleep(self):
		self.work.wait()

	def wakeUp(self):
		self.work.set()

	def cutHair(self, customer):
		#Set barber as busy 
		self.work.clear()

		print ('{0} is having a haircut'.format(customer.name))

		randhair = random.randrange(hair_min, hair_max+1)
		time.sleep(randhair)
		print ('{0} is done'.format(customer.name))


if __name__ == '__main__':
	cust = []

	cust.append(Customer('Tomas'))
	cust.append(Customer('Kristrun'))
	cust.append(Customer('Heidrun'))

	barber = Barber()

	shop = shop(barber, n=3)
	shop.openShop()

	while len(cust) > 0:
		c = cust.pop()	
		#New customer enters the shop
		shop.enter(c)
		cus_int = random.randrange(cus_min,cus_max+1)
		time.sleep(cus_int)