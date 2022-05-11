from threading import Thread, Lock, Event
import time, random

mutex = Lock()

#Interval in seconds
customerIntervalMin = 5
customerIntervalMax = 15
haircutDurationMin = 3
haircutDurationMax = 15

class BarberShop:
	waitingCustomers = []

	def __init__(self, barber, numberOfSeats):
		self.barber = barber
		self.numberOfSeats = numberOfSeats
		print ('Barberia tiene {0} sitios'.format(numberOfSeats))
		print ('Tiempo de espera por cliente {0}'.format(customerIntervalMin))
		print ('Máximo de intervalo por cliente  {0}'.format(customerIntervalMax))
		print ('Duración mínima de corte de pelo {0}'.format(haircutDurationMin))
		print ('Duración máxima de corte de pelo {0}'.format(customerIntervalMax))
		print ('---------------------------------------')

	def openShop(self):
		print ('La barbería está abierta')
		workingThread = Thread(target = self.barberGoToWork)
		workingThread.start()

	def barberGoToWork(self):
		while True:
			mutex.acquire()

			if len(self.waitingCustomers) > 0:
				c = self.waitingCustomers[0]
				del self.waitingCustomers[0]
				mutex.release()
				self.barber.cutHair(c)
			else:
				mutex.release()
				print ('BIEEEN!! el barbero se va a dormir, zzzzzz')
				barber.sleep()
				print ('El barbero se ha despertado  :=)')

	def enterBarberShop(self, customer):
		mutex.acquire()
		print ('>> {0} entró en la barbería y esta buscando un hueco'.format(customer.name))

		if len(self.waitingCustomers) == self.numberOfSeats:
			print ('El salón esta lleno, {0} está yéndose.'.format(customer.name))
			mutex.release()
		else:
			print ('{0} está esperando en la sala de espera'.format(customer.name)	)
			self.waitingCustomers.append(c)
			mutex.release()
			barber.wakeUp()

class Customer:
	def __init__(self, name):
		self.name = name

class Barber:
	barberWorkingEvent = Event()

	def sleep(self):
		self.barberWorkingEvent.wait()

	def wakeUp(self):
		self.barberWorkingEvent.set()

	def cutHair(self, customer):
		#Set barber as busy
		self.barberWorkingEvent.clear()

		print ('{0} se está cortando el pelo'.format(customer.name))

		randomHairCuttingTime = random.randrange(haircutDurationMin, haircutDurationMax+1)
		time.sleep(randomHairCuttingTime)
		print ('{0} está hecho'.format(customer.name))


if __name__ == '__main__':
	customers = []
	customers.append(Customer('Ruben'))
	customers.append(Customer('Sara'))
	customers.append(Customer('Alex'))
	customers.append(Customer('Alberto'))
	customers.append(Customer('Carlota'))
	customers.append(Customer('María'))
	customers.append(Customer('Raúl'))
	customers.append(Customer('María'))
	customers.append(Customer('David'))
	customers.append(Customer('Juan'))
	customers.append(Customer('Lorenzo'))
	customers.append(Customer('Julia'))
	customers.append(Customer('Juan'))
	customers.append(Customer('Laura'))
	customers.append(Customer('Tomas'))
	customers.append(Customer('Cristina'))
	customers.append(Customer('Juana'))

	barber = Barber()

	barberShop = BarberShop(barber, numberOfSeats=3)
	barberShop.openShop()

	while len(customers) > 0:
    #el método pop elimina el elemeto dado de la pila y devuelve
		c = customers.pop()
		#New customer enters the barbershop
		barberShop.enterBarberShop(c)
		customerInterval = random.randrange(customerIntervalMin,customerIntervalMax+1)
		time.sleep(customerInterval)