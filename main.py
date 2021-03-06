from threading import Thread, Lock, Event
import time, random

mutex = Lock()

#Definir una clase para el hilo
customerIntervalMin = 5
customerIntervalMax = 15
haircutDurationMin = 3
haircutDurationMax = 15

#Definir la clase Barbero para el hilo
class BarberShop:

	waitingCustomers = []
    #Definir el constructor de la clase
	def __init__(self, barber, numberOfSeats):
		self.barber = barber
		self.numberOfSeats = numberOfSeats
		print ('Barberia tiene {0} sitios'.format(numberOfSeats))
		print ('Tiempo de espera por cliente {0}'.format(customerIntervalMin))
		print ('Máximo de intervalo por cliente  {0}'.format(customerIntervalMax))
		print ('Duración mínima de corte de pelo {0}'.format(haircutDurationMin))
		print ('Duración máxima de corte de pelo {0}'.format(customerIntervalMax))
		print ('---------------------------------------')
    #Metod para cuando abre la barbería
	def openShop(self):
		print ('La barbería está abierta')
		workingThread = Thread(target = self.barberGoToWork)
		workingThread.start()
    #Método para cuando está trabajando el barbero y termina todos los clientes y se va a dormir
	def barberGoToWork(self):
		while True:
			mutex.acquire() #Se bloquea el acceso a la lista de clientes

			if len(self.waitingCustomers) > 0: #Si hay clientes en la lista
				c = self.waitingCustomers[0]
				del self.waitingCustomers[0]
				mutex.release()
				self.barber.cutHair(c)
			else: #Si no hay clientes en la lista
				mutex.release()
				print ('BIEEEN!! el barbero se va a dormir, zzzzzz')
				barber.sleep()
				print ('El barbero se ha despertado  :=)')

    #Método para cuando el cliente llega a la barbería
	def enterBarberShop(self, customer):
		mutex.acquire()
		print ('>> {0} entró en la barbería y esta buscando un hueco'.format(customer.name)) #Se imprime el nombre del cliente que está buscando hueco

		if len(self.waitingCustomers) == self.numberOfSeats: #Si el numero de clientes es igual al numero de sitios-> está lleno
			print ('El salón esta lleno, {0} está yéndose.'.format(customer.name))
			mutex.release()
		else:
			print ('{0} está esperando en la sala de espera'.format(customer.name)	) #Se imprime el nombre del cliente que está esperando porwue ha encontrado hueco en la barbería
			self.waitingCustomers.append(c)
			mutex.release()
			barber.wakeUp()

#Definir la clase Cliente para el hilo
class Customer:
	def __init__(self, name):
		self.name = name
#Definir la clase Barbero para el hilo
class Barber:
	barberWorkingEvent = Event() #Evento para saber si el barbero está trabajando o no

	def sleep(self): #Método para que el barbero se duerma
		self.barberWorkingEvent.wait()

	def wakeUp(self): # Método para que el barbero se despierte
		self.barberWorkingEvent.set()

	def cutHair(self, customer): #Método para que el barbero corte el pelo
		#Set barber as busy
		self.barberWorkingEvent.clear()

		print ('{0} se está cortando el pelo'.format(customer.name))

		randomHairCuttingTime = random.randrange(haircutDurationMin, haircutDurationMax+1) #Se genera un tiempo de corte de pelo aleatorio
		time.sleep(randomHairCuttingTime)
		print ('{0} está hecho'.format(customer.name)) #Se imprime que el cliente ya se cortó el pelo


if __name__ == '__main__':
    #Definir el nombre de clientes
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
    #Se imprime el nombre de los clientes
	while len(customers) > 0:
    #el método pop elimina el elemeto dado de la pila y devuelve
		c = customers.pop()
		#New customer enters the barbershop
		barberShop.enterBarberShop(c)
		customerInterval = random.randrange(customerIntervalMin,customerIntervalMax+1)
		time.sleep(customerInterval)