# Archivo: data_set_credito.py
# Este archivo contiene el metodo generador del data set de aprobacion de creditos.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029


def leer_data_set():
	try:
		f = open(nombre,'r')
		atributos = [0 for i in range(15)]
		resultado = []
		datos = f.readlines()
		for linea in datos:
			palabras = linea.split(',')
		f.close()
		return
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit(1)