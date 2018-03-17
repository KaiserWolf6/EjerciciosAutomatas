class Automata3():
	
	#Nos dice si la cadena fue aceptado	
	aceptado = False
	#El arreglo de caracteres de la cadena
	caracter = ['']
	#Contador para el arreglo
	cont = 0

	"""q0 Es el estado inicial del automata,
	   se direcciona a q1 si el caracter esta
	   en ese estado"""
	def q0(self):
		print "q0 es el estado inicial"
		if self.cont < len(self.caracter):
			if self.caracter[self.cont] == 'a':
				self.cont += 1
				self.q1()

	"""q1 Es un estado del automata,
	   se direcciona a q2 si el caracter esta
	   en ese estado"""
	def q1(self):
		print "En q1"
		if self.cont < len(self.caracter):
			if self.caracter[self.cont] == 'u':
				self.cont += 1
				self.q2()
	
	"""q2 Es un estado del automata,
	   se direcciona a q3 si el caracter esta
	   en ese estado"""
	def q2(self):
		print "En q2"
		if self.cont < len(self.caracter):
			if self.caracter[self.cont] == 't':
				self.cont += 1
				self.q3()

	"""q3 Es un estado del automata,
	   se direcciona a q4 si el caracter esta
	   en ese estado"""	
	def q3(self):
		print "En q3"
		if self.cont < len(self.caracter):
			if self.caracter[self.cont] == 'o':
				self.cont += 1
				self.q4()				

	"""q4 Es un estado del automata,
	   se direcciona a q5 si el caracter esta
	   en ese estado"""	
	def q4(self):
		print "En q4"
		if self.cont < len(self.caracter):
			if self.caracter[self.cont] == 'm':
				self.cont += 1
				self.q5()

	"""q5 Es un estado del automata,
	   se direcciona a q6 si el caracter esta
	   en ese estado"""
	def q5(self):
		print "En q5"
		if self.cont < len(self.caracter):
			if self.caracter[self.cont] == 'a':
				self.cont += 1
				self.q6()

	"""q6 Es un estado del automata,
	   se direcciona a q7 si el caracter esta
	   en ese estado"""
	def q6(self):
		print "En q6"
		if self.cont < len(self.caracter):
			if self.caracter[self.cont] == 't':
				self.cont += 1
				self.q7()

	"""q7 Es el estado final del automata,
	   si hay un caracter que inicia con a direcciona a q0 si no
	   termina en ese estado"""
	def q7(self):
		print "En q7 es el estado final"
		self.aceptado = True
		if self.cont < len(self.caracter):
			if self.caracter[self.cont] == 'a':
				self.cont += 1
				self.q0()
																
	"""Metodo que repite varias veces una cadena y regresa
	   una nueva cadena
	   + cadena la cadena automata
	   + repeticiones es el numero de veces que se
	     va a repetir la cadena"""
	def repeat(self, cadena, repeticiones):
		if repeticiones == 0 :
			print "Debes ingresar un valor mayor a cero"
		return cadena * repeticiones

	"""Inicializa las variables"""
	def iniciar(self):
		self.cont = 0
		self.aceptado = False
		self.q0()

a = Automata3()
print "Cuantas veces quieres que se repita la palabra automata: "
cadena = "automata"
aux = "automata"
repetir = input()
repetirCadena = a.repeat(aux, repetir)
nuevaCadena = cadena+repetirCadena
print "Nueva cadena: "
print(nuevaCadena)
a.caracter = list(nuevaCadena)
a.iniciar()
if a.aceptado:
	print "La cadena fue aceptado por el automata"
else:
	print "No aceptada"