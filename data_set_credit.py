# Archivo: data_set_credit.py
# Este archivo contiene el metodo generador del data set de aprobacion de creditos.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import sys

def read_data_set(name):
	try:
		f = open(name,'r')
		res = []
		data = f.readlines()
		for line in data:
			atributes = []
			words = line.split(',')
			for w in words:
				atributes.append(w)
			res.append(atributes)
		return res
		f.close()
		return
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit(1)
